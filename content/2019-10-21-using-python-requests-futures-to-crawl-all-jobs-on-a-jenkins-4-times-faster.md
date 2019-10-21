Title: Using python requests-futures to crawl all jobs on a Jenkins 4 times faster
Date: 2019-10-21 23:45
Tags: lang:en, python, open-source, oui.sncf, jenkins, algorithms, prog
Slug: using-python-requests-futures-to-crawl-all-jobs-on-a-jenkins-4-times-faster
---

![Jenkins logo as a ninja](images/2019/10/ninjenkins.svg)
<!-- Source: https://wiki.jenkins.io/display/JENKINS/Logo -->

At work, we needed to retrieve the full list of jobs a given [Jenkins](https://jenkins.io) instance was hosting.

Our first solution was to use the [jenkinsapi](https://jenkinsapi.readthedocs.io) Python package:

```python
import xml.etree.ElementTree as XmlElementTree
from jenkinsapi.jenkins import Jenkins


def get_all_jenkins_jobs(server_url):
    jenkins = Jenkins(server_url, lazy=True, timeout=30,
                      username=os.environ['JENKINS_USERNAME'], password=os.environ['JENKINS_PASSWORD'])
    all_jobs = []
    for job in jenkins.jobs.values():
        config_xml_content = job.get_config()  # performs an HTTP request to retrieve config.xml
        job_data = {'full_name': job.get_full_name(), 'url': job.url}
        job_data.update(extra_job_data_from_xml(config_xml_content))
        all_jobs.append(job_data)
    return all_jobs

def extra_job_data_from_xml(config_xml_content):
    xml_config = XmlElementTree.fromstring(config_xml_content)
    git_repo = xml_config.find('./definition/scm/userRemoteConfigs/hudson.plugins.git.UserRemoteConfig/url')
    if git_repo is None:
        return {}
    return {
        'scm': git_repo.text,
        'scm_http': 'https://' + git_repo.text.replace('git@', '').replace(':', '/').replace('.git', ''),
        'branch': xml_config.find('./definition/scm/branches/hudson.plugins.git.BranchSpec/name').text,
        'jenkinsfile': xml_config.find('./definition/scriptPath').text,
    }
```

This solution is nice and short.
But it has a main drawback: it is **very** slow.

Hence I decided to bypass the `jenkinsapi` package and make direct HTTP calls to the Jenkins API,
but this time using [requests-futures](https://github.com/ross/requests-futures) to perform requests asynchronously:

```python
from concurrent.futures import as_completed
import requests
from requests.adapters import HTTPAdapter
from requests_futures.sessions import FuturesSession


FOLDER_CLASSES = ('com.cloudbees.hudson.plugins.folder.Folder',
                  'org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject')


def get_all_jenkins_jobs_async(server_url):
    with FuturesSession() as session:
        session.auth = (os.environ['JENKINS_USERNAME'], os.environ['JENKINS_PASSWORD'])
        session.mount('https://', HTTPAdapter(max_retries=3))

        all_jobs_paths = []
        folder_paths_to_crawl = ['/']
        i = 0
        while folder_paths_to_crawl:
            print('Async breadth-first pass %s - Processing %s folders' % (i, len(folder_paths_to_crawl)))
            next_folder_paths_to_crawl = []
            futures = [session.get(server_url + folder_path + '/api/python',
                                   params={'tree': 'jobs[name,color,url]'})
                       for folder_path in folder_paths_to_crawl]
            for future in as_completed(futures):
                resp = future.result()
                path_prefix = resp.request.path_url[:-len('/api/python?tree=jobs%5Bname%2Ccolor%2Curl%5D')]
                for job in resp.json()['jobs']:
                    job_path = path_prefix + '/job/' + job['name']
                    if job['_class'] in FOLDER_CLASSES:
                        next_folder_paths_to_crawl.append(job_path)
                    else:
                        all_jobs_paths.append(job_path)
            folder_paths_to_crawl = next_folder_paths_to_crawl
            i += 1

        print('Now retrieving & parsing all config.xml files (%s)' % len(all_jobs_paths))
        def response_hook(resp, *_, **__):
            'This hook is executed in a dedicated thread'
            job_path = resp.request.path_url[:-len('config.xml')]
            resp.data = {
                'full_name': '/'.join(frag for frag in job_path.split('/') if frag not in ('', 'job')),
                'url': server_url + job_path,
            }
            resp.data.update(extra_job_data_from_xml(resp.text))
        session.hooks['response'] = response_hook
        all_jobs = []
        futures = [session.get(server_url + job_path + '/config.xml') for job_path in all_jobs_paths]
        for future in as_completed(futures):
            all_jobs.append(future.result().data)
        return all_jobs
```

The resulting code is definitively more verbose, but at least 4 times faster from my tests !

Now a word on the algorithmic approach taken here:
we need to crawl [a tree starting from its root](https://en.wikipedia.org/wiki/Tree_(graph_theory)#Rooted_tree).
For every node, if it is a leaf (an actual _WorkflowJob_) we collect it,
else we need to continue traversing its children.

My initial idea was to start new [concurrent Futures](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future)
for every child **inside its parent `Future` callback**. However this adds a lot of programatical complexity
([`cannot schedule new futures after shutdown`](https://github.com/python/cpython/blob/master/Lib/concurrent/futures/thread.py#L168) errors,
an added difficulty to wait on the last `Future` completion...).

In the end, I realized that because our Jenkins job tree has a very low depth,
a [breadth-first tree traversal](https://en.wikipedia.org/wiki/Breadth-first_search)
was a very good approach, with a known amount of `Future` requests being triggered for every depth level of the tree.
This is the solution implemented above.

I'd be happy to know if you already used `requests-futures` in such kind of tree-crawling scenario
(and if you compared it to other solutions),
or to answer any other feedback / question you may have.

PS: Many thanks to Vincent Lae for the initial idea ! 😉

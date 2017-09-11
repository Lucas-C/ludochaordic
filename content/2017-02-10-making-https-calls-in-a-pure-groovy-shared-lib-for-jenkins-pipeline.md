Title: Making HTTPS calls in a pure Groovy shared lib for Jenkins pipeline
Date: 2017-02-10 15:02
Tags: lang:en, jenkins, groovy, pipeline, https, voyages-sncf, prog
Slug: making-https-calls-in-a-pure-groovy-shared-lib-for-jenkins-pipeline
---
![Demonic version of the Jenkins logo](images/2017/02/butler-devil.png)

Recently I lost a lot of time on this. Hence I want to share a working solution, even if i cannot take the time to detail the issue.

I'm taking about writing reusable code for Jenkinsfiles : <https://jenkins.io/doc/book/pipeline/shared-libraries/>

One cannot simply use Groovy `HTTPBuilder`, because of Jenkins 2 custom Groovy interpreter that follow the *Continuation Passing Style* paradigm : <https://github.com/jenkinsci/workflow-cps-plugin#technical-design>

Hence the solution is to invoke the [http_request](https://jenkins.io/doc/pipeline/steps/http_request/) plugin :

    def jenkinsHttpGet(Map args) {
        def response = args.jenkinsWorkflowScript.invokeMethod 'httpRequest', [[args.url: url]] as Object[]
        if (response.status != 200) {
            jenkinsWorkflowScript.invokeMethod 'echo', [response.content] as Object[]
            throw new HttpResponseException(response.status, 'HTTP error')
        }
        response.content
    }

This function can be used like this in a Jenkinsfile :

    jenkinsHttpGet jenkinsWorkflowScript:this, url:'https://httpbin.org/get'

The `invokeMethod` trick makes it possible to invoke builtin functions from classes defined in shared libs.

Beware ! This code can trigger a `javax.net.ssl.SSLException: java.lang.RuntimeException: Could not generate DH keypair` if you are using Java 7. Upgrading to an 1.8 JVM for Jenkins fixed the issue.

You'll also have to take good care to make all your Groovy classes `Serializable`.

At [Voyages-Sncf](https://github.com/voyages-sncf-technologies), we are in the process of building a Groovy library of common tools that can be used both in CLI and in Jenkinsfiles.

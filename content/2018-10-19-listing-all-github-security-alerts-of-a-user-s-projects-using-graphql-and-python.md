Title: Listing all GitHub security alerts of a user's projects using GraphQL and Python
Date: 2018-10-19 19:00
Tags: lang:en, github, python, graphql, security, dependencies, prog
Slug: listing-all-github-security-alerts-of-a-user-s-projects-using-graphql-and-python
---
[Almost a year ago](https://blog.github.com/2017-11-16-introducing-security-alerts-on-github/), GitHub introduced security alerts. They are an awesome feature.

![Animation displaying the GitHub security alerts web interface](images/2018/10/github-security-alerts.gif)

They function as notifications you receive whenever a vulnerability affecting one of your project dependencies.

But long after receiving a notification, **how to list all security alerts affecting your repositories ?**

I didn't found an out-of-the box solution, so I wrote [a small Python script](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/github_graphql_get_reposecurityvulnerabilities.py) to perform this.

I wrote it to search for security alerts for all **source repositories** of a **single user**,
but it should be very easy to adapt it for a GitHub org or to also include forks.

Here is an example of output:
```
$ python3 github_graphql_get_reposecurityvulnerabilities.py
https://github.com/Lucas-C/tablut/network/alerts
- {"packageName": "randomatic", "affectedRange": "< 3.0.0", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2017-16028", "fixedIn": "3.0.0"}
https://github.com/Lucas-C/OuiJam2018/network/alerts
- {"packageName": "ssri", "affectedRange": "< 5.2.2", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2018-7651", "fixedIn": "5.2.2"}
- {"packageName": "hoek", "affectedRange": ">= 5.0.0,< 5.0.3", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2018-3728", "fixedIn": "5.0.3"}
- {"packageName": "mime", "affectedRange": "< 1.4.1", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2017-16138", "fixedIn": "1.4.1"}
- {"packageName": "parsejson", "affectedRange": "<=0.0.3", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2017-16113", "fixedIn": ""}
- {"packageName": "deep-extend", "affectedRange": "< 0.5.1", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2018-3750", "fixedIn": "0.5.1"}
- {"packageName": "randomatic", "affectedRange": "< 3.0.0", "externalReference": "https://nvd.nist.gov/vuln/detail/CVE-2017-16028", "fixedIn": "3.0.0"}
```

The script contacts [GitHub GraphQL API v4](https://developer.github.com/v4/),
and hence you'll need to [create a `GITHUB_OAUTH_TOKEN`](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)
in order to authenticated yourself with it. The only scope required is `repo > public_repo`.

The script also enable the [Repository Vulnerability Alerts Schema Preview](https://developer.github.com/v4/previews/#repository-vulnerability-alerts),
through an `Accept` HTTP header, as this feature is still in beta.

It was the first time I used the GraphQL query language.
It is very simple to grasp, but I have a complaint :
despite a [proposal](https://github.com/facebook/graphql/issues/271) discarded recently,
the language currently offers no way to filter the result with basic conditionals.
In my case I needed to process repositories that have vulnerability alerts,
but couldn't do so in GraphQL and had to filter them out in Python.

For a language which aims to [gives clients the power to ask for exactly what they need and nothing more](https://graphql.org),
this is a bit sad...

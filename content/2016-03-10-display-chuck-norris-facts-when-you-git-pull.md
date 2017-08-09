Title: Display Chuck Norris facts when you git pull !
Date: 2016-03-10 12:03
Tags: lang:en, git, hooks, chuck-norris, jenkins
Slug: display-chuck-norris-facts-when-you-git-pull
---
...in just one command :

	cd path/to/your/git/repo
    
	cat <<EOF >.git/hooks/pre-rebase
    #!/bin/sh
    echo -n \$'\x1b[36m' # start coloration (cyan)
    curl -s https://raw.githubusercontent.com/jenkinsci/chucknorris-plugin/master/src/main/java/hudson/plugins/chucknorris/FactGenerator.java | sed '1,/FACTS = {/d;s/^ \+"//;s/"..\?$//;/^$/,$d' | shuf -n 1
    echo -n \$'\x1b[0m' # end coloration
    EOF

And enjoy the message next time you `git pull` !

<img src="/lucas/wwcb/photos/chuck_norris_approve.gif">

Thanks to [jenkinsci/chucknorris-plugin](https://github.com/jenkinsci/chucknorris-plugin) developpers for collecting those facts.
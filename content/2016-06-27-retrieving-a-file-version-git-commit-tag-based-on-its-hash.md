Title: Retrieving a file version (git commit & tag) based on its hash
Date: 2016-06-27 19:06
Tags: lang:en, shell, hash, git, sha, version, tag-tag, prog
Slug: retrieving-a-file-version-git-commit-tag-based-on-its-hash
---
Today, I did some tests on a server where an old version of our project was deployed. At some point, I needed to identify which version of the code was there, and I wrote a pretty shell function to figure this out.

Yeah, I know what your thinking : <em>there must be another way</em>. Surely this information should be somewhere in your deployment system.
Probably. But that's no excuse to skip a good git scripting exercise !

<img src="images/wwcb/you-got-it-wrong-alphabet.jpg" title="You're doing it wrong">

Ok, so here is the situation :

- a git repository cloned on my development machine
- a remote server without git installed
- a readable file on this server that originates from the git repository

Now, the idea is to compute the file hash similarly to git, and then find a commit for which `git rev-parse` returns the same hash.

First thing first, lets build a function that does the same as `git hash-object` but does not require git. You can check [this SO answer](http://stackoverflow.com/questions/7225313/how-does-git-compute-file-hashes) or the details on how git compute blob hashes. Here is my solution:
```bash
git-hash-object () { # USAGE: git-hash-object [-t type] file
    local type=blob
    [ "$1" = "-t" ] && shift && type=$1 && shift
    # depending on your git eol/autocrlf settings,
    # you may want to substitute CRLFs by LFs first,
    # by using `perl -pe 's/\r$//g'` instead of `cat` in the next 2 commands
    local size=$(cat $1 | wc -c | sed 's/ .*$//')
    ( echo -en "$type $size\0"; cat "$1" ) | sha1sum | sed 's/ .*$//'
}
```

Ok, lets write our search function now:
```bash
git-identify-filehash () { # USAGE: git-identify file hash
    local file=${1?}
    local hash=${2?}
    git log --format="%h %s" $file | while read commit msg; do
        if [ $(git rev-parse $commit:$file) = "$hash" ]; then
            echo $commit $msg - oldest tag including this commit: \
                $(git tag --contains $commit | head -n 1)
            break
        fi
    done
}
```

Ok, I'm going to try this on the second-to-last version of `pre-commit` `main.py`, that is from commit [c3c98af](https://github.com/pre-commit/pre-commit/blob/c3c98af/pre_commit/main.py) at the time I'm writing :
```bash
$ wget http://github.com/pre-commit/pre-commit/raw/c3c98af/pre_commit/main.py
$ git hash-object main.py
e292c72c6c86e8809bd792a630e7f90ac811c385
# Lets pretend we are on a remote server without git:
$ git-hash-object main.py
e292c72c6c86e8809bd792a630e7f90ac811c385

# Now lets identify this file hash in our repository clone
$ git clone git@github.com:pre-commit/pre-commit.git
$ git-identify-filehash pre_commit/main.py e292c72c6c86e8809bd792a630e7f90ac811c385
c3c98af Support pre-commit from inside submodules - oldest tag including this commit: v0.7.1
```

![](images/wwcb/OMG.gif)

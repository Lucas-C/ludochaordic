Title: TIL zip files can contain comments
Date: 2016-01-08 12:01
Lang: en
Tags: lang:en, python, jq, zip, pythonchallenge, prog
Slug: til-zip-files-can-contain-comments
---
... and the standard UNIX tool `zipinfo` cannot display them !

![Photo of a zipper](images/2016/01/pythonchallenge-channel.jpg)

So here is Python one-liner to extract them, and other useful meta informations:

    python -c "import json, sys, zipfile; json.dump([{k: str(getattr(i, k)) for k in zipfile.ZipInfo.__slots__} for i in zipfile.ZipFile(sys.argv[1]).infolist()], sys.stdout)" $file.zip | jq .

Here, the outpout of the Python command is piped to  [`jq`](https://stedolan.github.io/jq/), a great tool to manipulate JSON on the command line. E.g. to extract only the filenames you can use: `jq -r .[].filename`.

Of course, one can also refactor this unreadable one-liner in a proper small script, or not use `jq`  and do the field selection in pure Python, but that's good starting point I guess :)

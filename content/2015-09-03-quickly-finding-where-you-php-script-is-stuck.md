Title: Quickly finding where you PHP script is stuck
Date: 2015-09-03 10:09
Lang: en
Tags: lang:en, gdb, php, stacktrace, stuck, wait, stdin, drush, unicode, prog
Slug: quickly-finding-where-you-php-script-is-stuck
---
First, install PHP debugging extensions for `gdb`, for example:
```
debuginfo-install php-5.6.8  # if you use yum
aptitude install php5-dbg    # if you use aptitude
```

Then simply:
```
php_version=5.6.8
php_script_pid=$(pgrep -f $php_script_name)
curl https://raw.githubusercontent.com/php/php-src/PHP-$php_version/.gdbinit >> ~/.gdbinit
gdb -p $php_script_pid
dump_bt executor_globals.current_execute_data
```

This will print **a stacktrace of PHP function calls**.

In my case, I found out my `drush` command was stuck waiting for text from `stdin`, because I gave it the wrong cli flag: `–y` instead of `-y`.

...

You noticed the difference ?
Yes, it's subttle and god damn confusing: the first argument contains the [unicode character EN-DASH](http://www.fileformat.info/info/unicode/char/2013/index.htm).

<img alt="So surprise he's spitting out his cereals" src="images/wwcb/cereal-guy-cereal-guy-spitting.png">

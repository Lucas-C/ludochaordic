Title: Quickly deleting all your old SauceLabs jobs
Date: 2015-02-17 08:02
Tags: lang:en, shell, xargs, perl, curl, saucelabs, prog
Slug: quickly-deleting-all-your-old-saucelabs-jobs
---
In a nutshell:

    SUN=$SAUCE_USERNAME; SAK=$SAUCE_ACCESSKEY
    curl -u $SUN:$SAAK https://saucelabs.com/rest/v1/$SUN/jobs?format=csv \
      | perl -wpe 's/\r$//' \
      | xargs -I{} curl -u $SUN:$SAK -X DELETE "https://saucelabs.com/rest/v1/$SUN/jobs/{}"

<img src="https://chezsoi.org/lucas/wwcb/photos/Climate-global_warming_level-_Earth_on_Fire.jpg" alt="Earth Kaboom">

Title: Free alerting-as-a-service drop-in replacement for mail command
Date: 2018-02-16 22:30
Tags: lang:en, alerting, service-monitoring, email, open-source, rollback, sentry, python, prog
Slug: free-alerting-as-a-service-drop-in-replacement-for-mail-command
---

On my personnal server, I used to send myself alerts by email using the handy standard [`mail`](https://linux.die.net/man/1/mail) command.
However, recently it appeared that my server became categorized as "spammer" by some online service providers,
due to the alerts frequency (a little bit more than one per day).

Hence, I got rid of the postfix package and cumbersome configuration and decided to find an alternative solution.
I hesitated between [Sentry](https://sentry.io), a big player in the alerting-as-a-service domain that has the big advantage to be open source
(and developped in Python !), and [rollbar](https://rollbar.com), for which I opted for because of its simplicty (and by curiosity).

Then, I only had to `pip install rollbar` on my server and create a `/usr/local/bin/mail` executable file with the following code:
```
#!/usr/bin/python
import rollbar, socket, sys
rollbar.init('rollbar token')
rollbar.report_message(socket.gethostname() + ' sent an email:' + ' '.join(sys.argv[1:]),
                       extra_data={'stdin': sys.stdin.read()})
```

Et voilà !

All my pre-existing scripts now send alerts to the rollbar web API,
I still receive email notifications from this service
**and** I now have an online web dashboard and extra functionnalities like alerts aggregation 🎉

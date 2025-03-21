Title: Record an existing voicemail message with Python & Twilio
Date: 2017-05-17 16:05
Lang: en
Tags: lang:en, python, twilio, prog
Slug: record-an-existing-voicemail-message-with-python
---
Last week, my father asked me if I could make a backup of an old lovely voicemail message he had,recorded by my sister when she was a kid.

I wrote a [short Python script](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/record_voicemail_with_twilio.py)
to accomplish this using [Twilio](https://www.twilio.com):
```python
twiml_url = 'https://handler.twilio.com/twiml/EH9515e9e0d2fb81f27d75a493225ae703'
client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
client.calls.create(to='+33241XXXXXX',
                    from_=client.incoming_phone_numbers.list()[0].phone_number,
                    record=True, url=twiml_url)
```

The twiml URL refers to a short XML file I created online on Twilio web console at <https://www.twilio.com/console/dev-tools/twiml-bins>:
```
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Pause length="30"/>
</Response>
```

After executing the script, I found the recorded audio message at <https://www.twilio.com/console/voice/dashboard>, where I was able to download it as MP3 or WAV:

![Screenshot of Twilio web console](images/2017/05/2017-05-17-18_40_04-Twilio-Console---Voice-Logs-Calls.png)

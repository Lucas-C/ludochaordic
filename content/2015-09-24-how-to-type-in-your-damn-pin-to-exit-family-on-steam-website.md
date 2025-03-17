Title: How to type in your damn PIN to exit Family View on Steam website
Date: 2015-09-24 23:09
Lang: en
Tags: lang:en, javascript, console, hack, steam, browser, pin, password, form, input
Slug: how-to-type-in-your-damn-pin-to-exit-family-on-steam-website
---
This evening I faced a really annoying bug: while able to exit Family View by entering my PIN in `Steam.exe`, I could not do so when trying to access the Steam website.
I simply could not pass the page "Adults, enter your PIN below to exit Family View." Neither with Chrome nor Firefox: the input field just silently ignored anything I typed in, and the "Submit" button stayed un-clickable.

<img alt="Angry face trying to resist" src="images/wwcb/angry-must-resist.jpeg">

After a quick look at the HTML, I simply used the following Javascript code in [my browser console](http://webmasters.stackexchange.com/questions/8525/how-to-open-the-javascript-console-in-different-browsers) to programatically enter my PIN and submit the form on this page :

```
$('steam_parental_password_box').value = '<your-4-digits-pin>'; SubmitForm()
```

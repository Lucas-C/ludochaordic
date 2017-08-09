Title: Overriding the <Enter> keydown behaviour in bootstrap-datepicker.js
Date: 2014-10-27 22:10
Tags: lang:en, javascript, jquerry, date, picker, event, keydown, enter, xpath, idempotent
Slug: overriding-the-enter-keydown-behaviour-in-bootstrap-datepicker-js
---
I've got many post ideas in the past two weeks, but none of them made it to the blog yet. While those scribbles are maturing, there is a short hack for the wonderful [datepicker](//eternicode.github.io/bootstrap-datepicker) pluging for [bootstrap.js](http://getbootstrap.com).

Given a datepicker initialized on a `<div id="date-picker">` like this:

```javascript
$('#date-picker').datepicker({
    language: 'fr',
    startDate: new Date(),
    todayHighlight: true,
});
```

Now that's how to override the default behaviour of the _**Enter**_ keydown event, that very annoyingly toggle on & off the user input:

```javascript
$('#date-selected').keydown(function (ev) {
    var keycode = (ev.keyCode ? ev.keyCode : ev.which);
    if (keycode == '13') {
        var dp = $('#date-picker').data('datepicker');
        // 1: we manually restore the input date so it's not toggled on/off
        dp.dates.pop(); // idempotent if no dates
        dp.dates.push(dp.viewDate);
        dp.setValue();
        // 2: we move to the next input field & close the picker
        $('input[id!="date-selected"]').first().focus();
        dp.hide();
    }
});
```
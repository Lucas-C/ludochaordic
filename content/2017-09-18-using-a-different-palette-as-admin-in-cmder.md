Title: Using a different palette as admin in cmder
Date: 2017-09-18 12:00
Tags: lang:en, windows, shell, cmder, theme, palette, solarized, prog
Slug: using-a-different-palette-as-admin-in-cmder
---

In the last years, [cmder](http://cmder.net) became my default console when I needed a `cmd.exe`-compatible Windows console.

Very often, I have a `cmder` window with a set of tabs under my standard Windows user, and another that I launch as admi, to switch on/off some services, e.g. MySQL daemon. And in the last weeks, I happened to confuse both a few times, leading me to create a few files owned by the Windows admin :(

Hence I decided to find a way to change the palette when in an admin `cmder` console.

I found what I was looking for among [its Github project issues](https://github.com/cmderdev/cmder/issues/370#issuecomment-263082897). Simply create a wrapping `cmder.bat` batch script in the your `cmder` root directory with this :
```
@echo off
set CMDER_ROOT=%~dp0
start %CMDER_ROOT%\vendor\conemu-maximus5\ConEmu.exe /icon "%CMDER_ROOT%\cmder.exe" /single /title Cmder /loadcfgfile "%CMDER_ROOT%\config\ConEmu-%USERNAME%.xml" /cmd cmd /k "%CMDER_ROOT%\vendor\init.bat cd %CD%
```

Notice that the name of the `ConEmu` configuration file (the underlying console emulator used by `cmder`) is `ConEmu-%USERNAME%.xml`.

Now, in the `config/` sub-directory, make a copy of the default `ConEmu.xml` file for every user you want to launch `cmder` as and name like that: `ConEmu-%USERNAME%.xml`.

Finally, launch `cmder` as admin, right click on the title bar of the window and choose "Settings", go to "Features > Colors" and choose another palette, like "Solarized Light". "Save settings" and you're done !

[![Screenshot of 2 cmder consoles with different users](images/2017/09/cmder-2-consoles-screenshot.png)](images/2017/09/cmder-2-consoles-screenshot.png))

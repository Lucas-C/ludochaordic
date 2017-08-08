Title: Colored logs in Python
Date: 2015-02-17 08:02
Tags: lang:en, python, color, logging, colorama, termcolor, wrapper
Slug: en-colored-logs-in-python
---
<u>_Disclaimer_:</u> this post was heaviliy inspired by the 2 following gists:

- [`color_log.py`](https://gist.github.com/brainsik/1238935) using `termcolor` recipes
- [`colorlog.py`](https://gist.github.com/kergoth/813057) using `colorama`

I loved the simplicity of the first, not having to manipulate any of the logging internal API, but I prefer `colorama` over `termcolor`.

Without further ado, there is my solution :

```python
import logging, sys
from colorama import Back, Fore, Style

LOG_FORMAT = "%(asctime)s - pid:%(process)s %(filename)s:%(lineno)d %(levelname)8s| %(message)s"

class ColorLogsWrapper(object):
    COLOR_MAP = {
        'debug': Fore.CYAN,
        'info': Fore.GREEN,
        'warning': Fore.YELLOW,
        'error': Fore.RED,
        'critical': Back.RED,
    }

    def __init__(self, logger):
        self.logger = logger

    def __getattr__(self, attr_name):
        if attr_name == 'warn':
            attr_name = 'warning'
        if attr_name not in 'debug info warning error critical':
            return getattr(self.logger, attr_name)
        log_level = getattr(logging, attr_name.upper())
         # mimicking logging/__init__.py behaviour 
        if not self.logger.isEnabledFor(log_level):
            return

        def wrapped_attr(msg, *args, **kwargs):
            style_prefix = self.COLOR_MAP[attr_name]
            msg = style_prefix + msg + Style.RESET_ALL
            # We call _.log directly to not increase the callstack
            # so that Logger.findCaller extract the corrects filename/lineno
            return self.logger._log(log_level, msg, args, **kwargs)
        return wrapped_attr

logging.basicConfig(stream=sys.stderr, format=LOG_FORMAT, level=logging.DEBUG)
LOGGER = ColorLogsWrapper(logging.getLogger(__name__))
LOGGER.debug('Debug')
LOGGER.info('Info')
LOGGER.warn('Warning')
LOGGER.error('Error')
LOGGER.critical('Critical')
```

Output:
<pre style="font-family: monospace;">$ py colored_logger.py 
2015-02-17 10:38:04,802 - pid:16089 colored_logger.py:39    DEBUG| <span style="color:darkcyan;">Debug</span>
2015-02-17 10:38:04,802 - pid:16089 colored_logger.py:40     INFO| <span style="color:darkgreen;">Info</span>
2015-02-17 10:38:04,802 - pid:16089 colored_logger.py:41  WARNING| <span style="color:gold;">Warning</span>
2015-02-17 10:38:04,802 - pid:16089 colored_logger.py:42    ERROR| <span style="color:darkred;">Error</span>
2015-02-17 10:38:04,802 - pid:16089 colored_logger.py:43 CRITICAL| <span style="background-color:red;color:white;">Critical</span>
</pre>

<img src="https://chezsoi.org/lucas/wwcb/photos/CouldWork_Creeper.jpg" alt"Could Work. You won't know if you don't try.">
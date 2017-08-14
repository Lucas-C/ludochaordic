Title: Django tips & tricks
Date: 2015-04-06 20:04
Tags: lang:en, python, html, color, debug, django, template, heroku, pythonrc, database_url, constants, dry, graph, prog
Slug: django-tips
---
I recently worked on a short website project using Django & Heroku. It was my very time using this Python framework, and I really liked it !

This is a compendium of tips & tricks that I, as a Django beginner, found quite useful :

# **Django enhanced shell**

To install it :
```
pip install django-extensions
```

I defined a useful shell alias to invoke with my custom `.pythonrc` :
```
alias djshell='PYTHONSTARTUP=$HOME/.pythonrc ./manage.py shell_plus --use-pythonrc'
```

The `.pythonrc` I use is available [on github](//github.com/Lucas-C/linux_configuration/blob/master/.pythonrc). It provides two useful features :

- it enables **command history**, stored in `~/.django_history`
- it defines a handy `load_fixture(filename)` function to load test data from the shell, data that will be automatically deleted when you exit it
<br><br>

# **djangocolors_formatter.py**

A simple drop-in one-file solution to get pretty colored logs output: [tiliv/django-colors-formatter](//github.com/tiliv/django-colors-formatter/blob/master/djangocolors_formatter/__init__.py)
<br><br>

# **A handy 'hasattribute' template filter**

Put the following code in `${my_app}/templatetags/hasattribute.py` :
```
from django import template
register = template.Library()
@register.filter(is_safe=True)
def hasattribute(obj, attr_name):
    return hasattr(obj, attr_name)
```

Then you can use it as an `if` condition in your templates :
```
{% load hasattribute %}
{% if user|hasattribute:'homeaddress' %}
    {{ user.homeaddress }}
{% endif %}
```
<br><br>

# **debug.py**

I find it very useful to enable a _debug_ mode when I'm developping, e.g. to get full stack traces when an exception arise. To enable it, I simply run `./manage.py runserver --settings debug`

For the magic to work, simply define a `debug.py` file in your project root directory, with your debug configuration. For example :
```
from path.to.your.project.settings import *
DEBUG = True
TEMPLATE_DEBUG = True
class InvalidVarException(object):
    def __mod__(self, missing):
        try:
            missing_str=unicode(missing)
        except:
            missing_str='Failed to create string representation'
        raise Exception('Unknown template variable %r %s' % (missing, missing_str))
    def __contains__(self, search):
        if search=='%s':
            return True
        return False
TEMPLATE_STRING_IF_INVALID = InvalidVarException()  # WARNING: do not catch undefined for-loops variables
```
<br><br>

# **Simply dealing with Heroku DATABASE_URL**
I wanted to use a local sqlite database in my developpement environment. But, when deployed on Heroku, the app has to pick up & follow the DB configuration provided by the `DATABASE_URL` environment variable.

Here is how to do it very easily :
```
from dj_database_url import parse as parse_db_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEST_DB_URL = 'sqlite:///' + BASE_DIR + '/local_test_db.sqlite3'

DATABASE_URL = os.environ.get('DATABASE_URL', TEST_DB_URL)
DATABASES = {'default': parse_db_url(DATABASE_URL)}
```
<br><br>

# **Easily making constants available in templates**

I used some pre-defined constants in the server-side logic, that I wanted to be accessible in the client-side HTML/javascript output.
As an example, one use case was that I needed to do some journey duration calculation on the server, and some visual map rendering of those journeys in JS. Both codes shared the same map boundaries, and I wanted to define those in only one place.

My solution was to create the following `${my_geo_app}/constants.py` file :
```
class BORDER_MAP(object):
    lat_nw = 49.0930256
    lon_nw = 1.9477209
    lat_se = 48.5442711
    lon_se = 2.9736786

# expose all the constants defined in this module in the templates
def context_processor(request):
    return globals()
```

Those constants can then be easily imported and used in the server-logic Python code.

And then, to make same available as constants in my templates, I simply had to tell django to parse this file for contexts, by adding the following in the project `settings.py` :
```
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    "my_geo_app.constants.context_processor",
)
```

Credits for the original idea: [this SO answer](//stackoverflow.com/a/433209/636849).
<br><br>

# **Templates checking**

I like to be able to check my HTML files for various kind of errors. As explained in [a previous post](//chezsoi.org/lucas/blog/2015/03/25/en-html-validation-and-converting-a-bash-script-to-python/), this is a process easy to automate, and one way to deal with "mustaches" template variables is simply to ignore them.

But I wanted to ensure that my templates did not use mistyped or undefined variables. Hence I built a small script that :

- given a dictionary of variables test values, check that no template contains undefined variable.
- render the templates with those test values, so that the output HTML can be then analyzed by other checkers

The script is [on github](//github.com/Lucas-C/linux_configuration/blob/master/languages/python/render_all_django_templates.py).

And here is an example of `tplt_test_context.py` configuration file defining some variables values :
```
DJANGO_SETTINGS_MODULE = 'my_app.settings'

def get_context_dict():
    # Project-specific imports must be done after django.setup()
    from profiles.models import User
    from startup_pages.forms import ContactAndRegisterForm

    users = list(User.objects.select_related('user__homeaddress'))
    return {
        'users': users,
        'contactform': ContactAndRegisterForm(),
        'src_username': users[1].username,
    }
```

And an example of output:
<pre>/path/to/project/templates/templates/allusers.html
<span style="color:green;">  -> ok: users, STATIC_URL</span>
/path/to/project/templates/entrer-en-contact.html
<span style="color:green;">  -> ok: contactform, STATIC_URL</span>
/path/to/project/templates/dest-summary.html
<span style="color:green;">  -> ok: STATIC_URL</span>
<span style="color:red;">  -> missing: dest_username</span>
</pre>
<br><br>

# **Generate a pretty graph of your models relations**

```
pip install pyparsing==1.5.7 && pip install pydot && ./manage.py graph_models -a -g -o pretty_models_visualization.png
```
<br><br>

# **More tips & tricks for the Frenchies**
- http://sametmax.com/mieux-que-python-virtualenvwrapper-pew/
- http://www.miximum.fr/checklist-bonnes-pratiques-django.html.html

**EDIT [16/05/2015]**: another good read: [Django anti-patterns](http://docs.quantifiedcode.com/python-code-patterns/django/index.html)

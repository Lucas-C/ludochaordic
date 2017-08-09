Title: AngularJS console debugging tips + pre-commit hooks
Date: 2015-05-30 14:05
Tags: lang:en, debug, console, angularjs, directive, service, scope, controller, selector
Slug: angularjs-console-debugging-tips-and-pre-commit-hooks
---
Just some handy accessors for the brower console :

```
var myScope = $('#directive > select.or').scope()
var $rootScope = $('body').scope() // if <body> has the 'ng-app' attribute
var myController = $('#directive > select.or').controller()

var injector = $(document.body).injector()
var myService = injector.get('myServiceName')
```

<br>

And there are 3 handy [pre-commit](https://chezsoi.org/lucas/blog/2015/05/16/en-git-pre-commit-hooks/) hooks :
```
- repo: local
  hooks:
  - id: angular-forbid-apply
    name: In AngularJS, use $digest over $apply
    language: pcre
    entry: $apply
    files: \.js$
  - id: angular-forbid-ngrepeat-without-trackby
    name: In AngularJS, ALWAYS use 'track by' with ng-repeat
    language: pcre
    entry: ng-repeat(?!.*track by)
    files: \.html$
  - id: angular-forbid-ngmodel-with-no-dot
    name: In AngularJS, "Whenever you have ng-model there’s gotta be a dot in there somewhere"
    language: pcre
    entry: ng-model="?[^.]+[" ]
    files: \.html$
```

You can find the justification for the two first hooks in [those great slides by Nir Kaufman](http://fr.slideshare.net/nirkaufman/angularjs-performance-production-tips).

The second will help you to detect [a nested scope gotcha](http://jimhoskins.com/2012/12/14/nested-scopes-in-angularjs.html) in AngularJS identified by Miško Hevery:

> "Whenever you have ng-model there’s gotta be a dot in there somewhere. If you don’t have a dot, you’re doing it wrong"

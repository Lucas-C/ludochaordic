Title: Disabling error stack traces with SpringBoot, but only in prod
Date: 2015-10-29 12:10
Tags: lang:en, yaml, java, controller, springboot, exception, http, stacktrace, profile, conditional, property, war
Slug: disabling
---


Simply add the following class to your project. It will be automatically registered at start-up if you use the [`@EnableAutoConfiguration` annotation](http://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-auto-configuration.html) :

```
@ControllerAdvice  // Makes this the default behaviour of all controllers
@ConditionalOnProperty(prefix = "app", name = "disable-default-exception-handling")
class GlobalControllerExceptionHandler {
    @ExceptionHandler(Exception.class)  // Catch any exception
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)  // Returns an error code 500
    public void handleException() {
    }
}
```

The nice trick is that you can the define your production settings as the default properties in your `application.yml` :
```
app:
  disable-default-exception-handling: true
error:
  whitelabel:
    enabled: false
```

Then, when you run your SpringBoot application on your local machine, select the dev Spring profile with `-Dspring.profiles.active=dev` and put the following in `application-dev.yml` :
```
app:
  disable-default-exception-handling: false
error:
  whitelabel:
    enabled: true
```

I tested it with a [`.war`](//en.wikipedia.org/wiki/WAR_(file_format)) deployed under Apache Tomcat 7.0.52. Most of the code comes straight from the [official documentation](//spring.io/blog/2013/11/01/exception-handling-in-spring-mvc), I only added the `@ConditionalOnProperty`.

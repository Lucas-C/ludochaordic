Title: JSONP & exceptions with Spring web 4
Date: 2017-05-19 12:05
Tags: lang:en, java, spring, jsonp, exception, javascript, callback, prog
Slug: properly-handling-exceptions
---
Since Spring 4.1, it is really easy to enable [JSONP](https://en.wikipedia.org/wiki/JSONP) on an API controller:
```java
@RestController
@RequestMapping(value = "/")
public class MyController {

    @ControllerAdvice
    static class JsonpAdvice extends AbstractJsonpResponseBodyAdvice {
        public JsonpAdvice() {
            super("callback"); // name of the query parameter to use
        }
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public MyAPIResult getStuff(...) {
        ...
    }
}
```

There is no RFC for JSONP. It is simply a recipe, without any reference document for implementation best practices.

Specifically, error handling can be difficult: **if an API return a 4XX or 5XX error, the JSONP callback cannot catch them** and will simply never be called, whereas the API actually responded.

In order to fix this, a solution is to make your API handle exceptions differently when a `callback` parameter is provided, and else to respond with 4XX/5XX HTTP codes as a REST API should do.

For example, **in case of an error your API can pass to the Javascript `callback` an `Error` instead of a JSON object**. The calling code can then react to errors as it wishes:
```javascript
window.jsonp_callback = function (response) {
    if (response instanceof Error) {
        ...handle API error response
    } else {
        ...handle API successful response
    }
}
```

On the server side, with Spring, this can be accomplished with an `@ExceptionHandler` annotation:
```java
@ControllerAdvice // Handle exceptions raised in all controllers
class GlobalControllerExceptionHandler {

    @ExceptionHandler(NotFoundException.class) // 404
    public ResponseEntity handleNotFoundException(NotFoundException exception,
                                                  HttpServletRequest request) {
        LOGGER.error("Error 404", exception);
        return createErrorResponse(HttpStatus.NOT_FOUND,
                                   request.getParameterMap(),
                                   exception.getMessage());
    }

    @ExceptionHandler(Exception.class)  // Catch any other exception -> 500
    public ResponseEntity handleException(Exception exception,
                                          HttpServletRequest request) {
        LOGGER.error("Error 500", exception);
        return createErrorResponse(HttpStatus.INTERNAL_SERVER_ERROR,
                                   request.getParameterMap(),
                                   exception.getMessage());
    }

    static private ResponseEntity createErrorResponse(HttpStatus errorStatus,
                                                      Map<String, String[]> params,
                                                      String errorMsg) {
        if (params.containsKey("callback")) {
            final String jsError = String.format("%s(new Error('%d: %s'))",
                                                 params.get("callback")[0],
                                                 errorStatus.value(),
                                                 escapeEcmaScript(errorMsg));
            return new ResponseEntity<>(jsError, HttpStatus.OK);
        }
        return new ResponseEntity<>(createJsonResponse(errorMsg), errorStatus);
    }

    static private String createJsonResponse(String errorMsg) {
        final Map<String, Object> jsonData = new HashMap<>();
        jsonData.put("error", errorMsg);
        return StringFormatUtils.multilinesPrettyFormat(jsonData);
    }
}
```

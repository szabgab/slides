# Test Event for API Gateway


* Before we fix the code, we can fix the test:

```
{
    "queryStringParameters" : {
        "name": "Foo Bar"
    }
}
```

* Try this using the "Test" button.

Also, try it from the console using `curl` or in your browser (use your own URL).

* curl 'https://qspmdah6oj.execute-api.us-east-1.amazonaws.com/v0/hello?name=Foo%20Bar'

```
{"message": "Hello Foo Bar!"}
```




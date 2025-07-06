# GET URL that does not exist (404 error)


Here we deliberately created a URL that does not exist on the HTTPbin web server. In this case the response was not Net::HTTPOK,
so Ruby executed the `else` part of our program. The code was `404` and the response message was `NOT FOUND`. I am sure you have already
encountered links that returned this error message. BTW you can try to visit the URLs using your regular browser as well to see the same response.

{% embed include file="src/examples/net-http/get_response_get_httpbin_error.rb" %}

The output was:

```
404
NOT FOUND
```



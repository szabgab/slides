# GET URL that pretends to crash (500)


Generating `500 INTERNAL SERVER ERROR` will be more fun, but we don't have to do anything special. Just send a `GET` request to the `/status/500` end-point.

{% embed include file="src/examples/net-http/get_response_get_httpbin_500.rb" %}

The output was:

```
500
INTERNAL SERVER ERROR
```



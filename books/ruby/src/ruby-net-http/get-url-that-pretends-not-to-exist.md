# GET URL that pretends not to exist (404)


Previously we got a `404 NOT FOUND` HTTP response because we tried to access a page that really does not exist.
It was easy to generate a 404 error, but it would be a lot harder - effectively impossible to consistently get a web-site to
return other HTTP error messages. eg. While we generally would want to avoid getting a `500 INTERNAL SERVER ERROR` but for testing
purposes (for our client code) we might want to be able to consistently create it.

Luckily HTTPbin provide the service to fake any HTTP status code.

First let's see how does it generate `404 NOT FOUND` message:

{% embed include file="src/examples/net-http/get_response_get_httpbin_404.rb" %}

Here, instead of the `/get` end-point we access the `/status/CODE` end-point replacing the CODE with the desired HTTP status code.
HTTPbin will respond with that status code.

The output was:

```
404
NOT FOUND
```



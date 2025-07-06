# Sending a POST request

* POST
* post_form

There is more to do with `GET` requests, but before we go on, let's also see how to send simple `POST` requests.

First of all HTTPbin expects the `POST` requests to arrive to a different end-point called, `/post`.

In order to send a `POST` request we call the `post_form` method. Pass the URI to it and a hash of the data.
The hash can be empty but it mist be provided. In our case I just provided it with two keys-value pairs.

{% embed include file="src/examples/net-http/post_response_get_httpbin.rb" %}

This is the response. HTTPbin was kind enough to send back the form-data so we can verify that it was sent and received properly.

{% embed include file="src/examples/net-http/post_response_get_httpbin.out" %}


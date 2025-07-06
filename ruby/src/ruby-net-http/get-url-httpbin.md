# GET URL httpbin


* get_response
* URI
* Net::HTTP
* HTTPSuccess

Let's start with a really simple example:

This is a plain GET requests

{% embed include file="src/examples/net-http/get_response_get_httpbin.rb" %}

The `get_response` method of the [Net::HTTP](https://ruby-doc.org/3.1.2/stdlibs/net/Net/HTTP.html) class.

The response that we stored in a variable cleverly named `response` can be interrogated to see if the response was a success or failure.
It is an instance of a [Net::HTTPResponse](https://ruby-doc.org/3.1.2/stdlibs/net/Net/HTTPResponse.html) class.
In case it is a success we print the body of the response and see this:

{% embed include file="src/examples/net-http/get_response_get_httpbin.out" %}

For the other case see the next example.



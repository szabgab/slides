# Show request headers


Often you'll be interested to see if you managed to set the headers as expected by an API. For that HTTPbin provides the `/headers` end-point.

First let's see what happens if we send a plain request to this end-point?

{% embed include file="src/examples/net-http/get_request_headers_httpbin.rb" %}

This is the header as our Ruby code sent it. (Note the User Agent being `Ruby`)

{% embed include file="src/examples/net-http/get_request_headers_httpbin.out" %}


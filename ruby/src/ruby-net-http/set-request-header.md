# Set request headers

* initheader

Finally we get to the point where we can set the headers in the request. Actually it is pretty easy to do so.
We just need to pass a new parameter called `initheader` with a hash of the header keys and values we would like to set.

This way we can add new fields to the header and we can replace existing ones. For example here we set the `User-Agent`
to `Internet Explorer 6.0`.

{% embed include file="src/examples/net-http/set_request_headers_httpbin.rb" %}

In the response we can see that the fields were set as expected.

{% embed include file="src/examples/net-http/set_request_headers_httpbin.out" %}

As you might know every time you access a web site it will log the request in a log file, usually including the User-Agent as well.
This way you could generate lots of request to a web site making their stats show that Internet Explorer 6.0 is back in popularity.

Don't do it!



# Setting header in POST request


If we also would like to set fields in the header we need a slightly more complex way of writing this:

First we need to create a request object using `Net::HTTP::Post`.
Then add the form data using the `set_form_data` method.
Finally add a few key-value pairs directly to the request.

Then we need to `start` the HTTP session and send the request using the `request` method.`

When we called `start` we had to supply the hostname and the port manually and because our URL is https (and not http)
we also need to set `:use_ssl => true` in order for this to work.

{% embed include file="src/examples/net-http/post_header_ssl_httpbin.rb" %}
{% embed include file="src/examples/net-http/post_header_ssl_httpbin.out" %}



# net/http
{id: net-http}

## GET URL
{id: net-http-get-url}

![](examples/net-http/get.rb)

## GET URL httpbin
{id: get-url-httpbin}

[httpbin](http://httpbin.org/) is an excellent web site to try to write http requests against.

This is a plain GET requests

![](examples/net-http/get_response_get_httpbin.rb)

This is the response:

![](examples/net-http/get_response_get_httpbin.out)

## GET URL that does not exist (404 error)
{id: get-urr-that-does-not-to-exist}

![](examples/net-http/get_response_get_httpbin_error.rb)

404

## GET URL that pretends not to exist (404)
{id: get-url-that-pretends-not-to-exist}

![](examples/net-http/get_response_get_httpbin_404.rb)

404

## GET URL that pretends not to crash (500)
{id: get-url-that-pretendsa-to-crash}

![](examples/net-http/get_response_get_httpbin_500.rb)

500


## Show request headers
{id: show-request-headers}

![](examples/net-http/show_request_headers_httpbin.rb)
![](examples/net-http/show_request_headers_httpbin.out)

## Set request headers
{id: set-request-header}

![](examples/net-http/set_request_headers_httpbin.rb)
![](examples/net-http/set_request_headers_httpbin.out)


# net/http
{id: net-http}

## GET URL httpbin
{id: get-url-httpbin}
{i: get_response}
{i: URI}
{i: Net::HTTP}
{i: HTTPSuccess}

[httpbin](http://httpbin.org/) is an excellent web site to try to write HTTP requests against. You can even run it on your own computer if you'd like to avoid making external network calls.
It allows you to send various types of HTTP requests and will send you a response in a way that you can verify that your request was sent properly.

Part of the goal of this service is to allow you to generate error conditions and see how your web-client code handles a situation where the remote server returns an error code.

Let's start with a really simple example:

This is a plain GET requests

![](examples/net-http/get_response_get_httpbin.rb)

The `get_response` method of the [Net::HTTP](https://ruby-doc.org/stdlib-2.7.1/libdoc/net/http/rdoc/Net/HTTP.html) class.

The response that we stored in a variable cleverly named `response` can be interrogated to see if the respons was a success or failure.
It is an instance of a [Net::HTTPResponse](https://ruby-doc.org/stdlib-2.7.1/libdoc/net/http/rdoc/Net/HTTPResponse.html) class.
In case it is a success we print the body of the response and see this:

![](examples/net-http/get_response_get_httpbin.out)

For the other case see the next example.

## GET URL that does not exist (404 error)
{id: get-urr-that-does-not-to-exist}

Here we deliberatly created a URL that does not exist on the HTTPbin web server. In this case the response was not Net::HTTPOK,
so Ruby executed the `else` part of our program. The code was `404` and the response message was `NOT FOUND`. I am sure you have already
encountered links that returned this error message. BTW you can try to visit the URLs using your regular browser as well to see the same response.

![](examples/net-http/get_response_get_httpbin_error.rb)

The output was:

```
404
NOT FOUND
```

## GET URL that pretends not to exist (404)
{id: get-url-that-pretends-not-to-exist}

Previously we got a `404 NOT FOUND` HTTP response because we tried to access a page that really does not exist.
It was easy to generate a 404 error, but it would be a lot harder - effectively impossble to consistently get a web-site to
return other HTTP error messages. eg. While we generally would want to avoid getting a `500 INTERNAL SERVER ERROR` but for testing
puporses (for our client code) we might want to be able to consistently create it.

Luckily HTTPbin provide the service to fake any HTTP status code.

First let's see how does it generat `404 NOT FOUND` message:

![](examples/net-http/get_response_get_httpbin_404.rb)

Here, instead of the `/get` end-point we access the `/status/CODE` end-point replacing the CODE with the desired HTTP status code.
HTTPbin will respond with that status code.

The output was:

```
404
NOT FOUND
```

## GET URL that pretends to crash (500)
{id: get-url-that-pretendsa-to-crash}

Generating `500 INTERNAL SERVER ERROR` will be more fun, but we don't have to do anything special. Just send a `GET` request to the `/status/500` end-point.

![](examples/net-http/get_response_get_httpbin_500.rb)

The putput was:

```
500
INTERNAL SERVER ERROR
```

## Show request headers
{id: show-request-headers}

Often you'll be interested to see if you managed to set the headers as expected by an API. For that HTTPbin provides the `/headers` end-point.

First let's see what happens if we send a plain request to this end-point?

![](examples/net-http/get_request_headers_httpbin.rb)

This is the header as our Ruby code sent it. (Note the User Agent being `Ruby`)

![](examples/net-http/get_request_headers_httpbin.out)

## Get request headers using FireFox
{id: get-request-headers-with-firefox}

Just to compare, when I visited [this url](https://httpbin.org/headers) using [FireFox](https://www.mozilla.org/en-US/firefox/new/), my default browser I get the
following results:

```
{
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Host": "httpbin.org",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "X-Amzn-Trace-Id": "Root=1-6394b5d7-395b7a2a377ea2df7dd4dbe8"
  }
}
```

Here the User-Agent is more detailed.

## Get request headers using curl
{id: get-request-headers-using-curl}

Using [curl](https://curl.se/)

```
$ curl https://httpbin.org/headers
```

I got the following response:

```
{
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.81.0",
    "X-Amzn-Trace-Id": "Root=1-6394b68a-65bd2c145c2304274a314120"
  }
}
```

## Set request headers
{id: set-request-header}
{i: initheader}

Finally we get to the point where we can set the headers in the request. Actually it is pretty easy to do so.
We just need to pass a new parameter called `initheader` with a hash of the header keys and values we would like to set.

This way we can add new fields to the header and we can replace existing ones. For example here we set the `User-Agent`
to `Internet Explorer 6.0`.

![](examples/net-http/set_request_headers_httpbin.rb)

In the response we can see that the fields were set as expected.

![](examples/net-http/set_request_headers_httpbin.out)

As you might know every time you access a web site it will log the request in a log file, usuallu including the User-Agent as well.
This way you could generate lots of request to a web site making their stats show that Internet Explorer 6.0 is back in popularity.

Don't do it!

## GET URL
{id: net-http-get-url}

![](examples/net-http/get.rb)



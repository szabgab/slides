# net/http
{id: net-http}

## API requests
{id: ruby-api-requests}

* API
* Net::HTTP
* [HTTPbin](http://httpbin.org/)

{aside}
In order to be able to interact with web applications one needs to be able to write proper HTTP requests to access the API of the web application.

Ruby has a library called Net::HTTP that can provide the tools to write these call.

[httpbin](http://httpbin.org/) is an excellent web site to try to write HTTP requests against. You can even run it on your own computer if you'd like to avoid making external network calls.
It allows you to send various types of HTTP requests and will send you a response in a way that you can verify that your request was sent properly.

Part of the goal of this service is to allow you to generate error conditions and see how your web-client code handles a situation where the remote server returns an error code.
{/aside}

## GET URL httpbin
{id: get-url-httpbin}
{i: get_response}
{i: URI}
{i: Net::HTTP}
{i: HTTPSuccess}

Let's start with a really simple example:

This is a plain GET requests

![](examples/net-http/get_response_get_httpbin.rb)

The `get_response` method of the [Net::HTTP](https://ruby-doc.org/3.1.2/stdlibs/net/Net/HTTP.html) class.

The response that we stored in a variable cleverly named `response` can be interrogated to see if the response was a success or failure.
It is an instance of a [Net::HTTPResponse](https://ruby-doc.org/3.1.2/stdlibs/net/Net/HTTPResponse.html) class.
In case it is a success we print the body of the response and see this:

![](examples/net-http/get_response_get_httpbin.out)

For the other case see the next example.

## GET URL that does not exist (404 error)
{id: get-urr-that-does-not-to-exist}

Here we deliberately created a URL that does not exist on the HTTPbin web server. In this case the response was not Net::HTTPOK,
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
It was easy to generate a 404 error, but it would be a lot harder - effectively impossible to consistently get a web-site to
return other HTTP error messages. eg. While we generally would want to avoid getting a `500 INTERNAL SERVER ERROR` but for testing
purposes (for our client code) we might want to be able to consistently create it.

Luckily HTTPbin provide the service to fake any HTTP status code.

First let's see how does it generate `404 NOT FOUND` message:

![](examples/net-http/get_response_get_httpbin_404.rb)

Here, instead of the `/get` end-point we access the `/status/CODE` end-point replacing the CODE with the desired HTTP status code.
HTTPbin will respond with that status code.

The output was:

```
404
NOT FOUND
```

## GET URL that pretends to crash (500)
{id: get-url-that-pretends-to-crash}

Generating `500 INTERNAL SERVER ERROR` will be more fun, but we don't have to do anything special. Just send a `GET` request to the `/status/500` end-point.

![](examples/net-http/get_response_get_httpbin_500.rb)

The output was:

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

## Get request headers using Firefox
{id: get-request-headers-with-firefox}

Just to compare, when I visited [this url](https://httpbin.org/headers) using [Firefox](https://www.mozilla.org/en-US/firefox/new/), my default browser I get the
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

As you might know every time you access a web site it will log the request in a log file, usually including the User-Agent as well.
This way you could generate lots of request to a web site making their stats show that Internet Explorer 6.0 is back in popularity.

Don't do it!

## Sending a POST request
{id: sending-post-request}
{i: POST}
{i: post_form}

There is more to do with `GET` requests, but before we go on, let's also see how to send simple `POST` requests.

First of all HTTPbin expects the `POST` requests to arrive to a different end-point called, `/post`.

In order to send a `POST` request we call the `post_form` method. Pass the URI to it and a hash of the data.
The hash can be empty but it mist be provided. In our case I just provided it with two keys-value pairs.

![](examples/net-http/post_response_get_httpbin.rb)

This is the response. HTTPbin was kind enough to send back the form-data so we can verify that it was sent and received properly.

![](examples/net-http/post_response_get_httpbin.out)


## Setting header in POST request
{id: setting-header-in-post-request}

If we also would like to set fields in the header we need a slightly more complex way of writing this:

First we need to create a request object using `Net::HTTP::Post`.
Then add the form data using the `set_form_data` method.
Finally add a few key-value pairs directly to the request.

Then we need to `start` the HTTP session and send the request using the `request` method.`

When we called `start` we had to supply the hostname and the port manually and because our URL is https (and not http)
we also need to set `:use_ssl => true` in order for this to work.

![](examples/net-http/post_header_ssl_httpbin.rb)
![](examples/net-http/post_header_ssl_httpbin.out)


## Debugging a failed request
{id: debugging-a-failed-request}

{aside}
In the previous example you saw that I had to set `:use_ssl => true`, but it took some time to figure it out.
The main problem was that in case of failure my previous code only printed the HTTP status code that was 400.

I read the documentation several times and tried various combinations of the code till it occurred to be that maybe
there is some hint in the `body` of the response. So I changed the code to print that in case of failure.
{/aside}

![](examples/net-http/post_header_httpbin.rb)

This was the response:

![](examples/net-http/post_header_httpbin.out)

That allowed me to understand that the issue is around the use of ssl: http vs https. First I tried the same code
replacing the URL by one that uses http:

```
url = 'http://httpbin.org/post'
```

This worked.

At this point I understood I need to search for something about ssl, and that's how I found out that I had to pass `:use_ssl => true`.

So remember, at least for debugging, it can be useful to print the content of the body even in the case of error.


## GET URL
{id: net-http-get-url}

![](examples/net-http/get.rb)



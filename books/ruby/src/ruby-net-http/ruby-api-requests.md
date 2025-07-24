# API requests


* API
* Net::HTTP
* [HTTPbin](http://httpbin.org/)


In order to be able to interact with web applications one needs to be able to write proper HTTP requests to access the API of the web application.

Ruby has a library called Net::HTTP that can provide the tools to write these call.

[httpbin](http://httpbin.org/) is an excellent web site to try to write HTTP requests against. You can even run it on your own computer if you'd like to avoid making external network calls.
It allows you to send various types of HTTP requests and will send you a response in a way that you can verify that your request was sent properly.

Part of the goal of this service is to allow you to generate error conditions and see how your web-client code handles a situation where the remote server returns an error code.



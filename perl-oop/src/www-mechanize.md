# WWW::Mechanize, and example using OOP

Let's take a look at an example of using a Perl module which was written in Object Oriented style. I am quite sure you have encountered many similar modules.
We are looking at the [WWW::Mechanize](https://metacpan.org/pod/WWW::Mechanize) module that makes it easy to send HTTP requests to web servers.

This is the full code:

{% embed include file="src/examples/www-mechanize/demo.pl" %}

We can use it on the command line by passing 

```
$ perl demo.pl https://httpbin.org/get

200 OK

Status: 200
200 OK

Connection: close
Date: Sun, 22 Jun 2025 12:40:45 GMT
Server: gunicorn/19.9.0
Content-Length: 271
Content-Type: application/json
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Client-Date: Sun, 22 Jun 2025 12:38:26 GMT
Client-Peer: 34.198.95.5:443
Client-Response-Num: 1
Client-SSL-Cert-Issuer: /C=US/O=Amazon/CN=Amazon RSA 2048 M02
Client-SSL-Cert-Subject: /CN=httpbin.org
Client-SSL-Cipher: ECDHE-RSA-AES128-GCM-SHA256
Client-SSL-Socket-Class: IO::Socket::SSL
Client-SSL-Version: TLSv1_2

{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "gzip", 
    "Host": "httpbin.org", 
    "User-Agent": "WWW-Mechanize/2.19", 
    "X-Amzn-Trace-Id": "Root=1-6857f9cd-788661eb40c56ecd14d4d272"
  }, 
  "origin": "46.120.8.126", 
  "url": "https://httpbin.org/get"
}
```

```
$ perl demo.pl https://httpbin.org/status/500

500 INTERNAL SERVER ERROR
500
500 INTERNAL SERVER ERROR

Connection: close
Date: Sun, 22 Jun 2025 12:41:15 GMT
Server: gunicorn/19.9.0
Content-Length: 0
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Client-Date: Sun, 22 Jun 2025 12:38:56 GMT
Client-Peer: 18.209.97.55:443
Client-Response-Num: 1
Client-SSL-Cert-Issuer: /C=US/O=Amazon/CN=Amazon RSA 2048 M02
Client-SSL-Cert-Subject: /CN=httpbin.org
Client-SSL-Cipher: ECDHE-RSA-AES128-GCM-SHA256
Client-SSL-Socket-Class: IO::Socket::SSL
Client-SSL-Version: TLSv1_2
```


[HTTP::Response](https://metacpan.org/pod/HTTP::Response)

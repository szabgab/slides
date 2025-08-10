# Add route returning JSON

* lib/D2/Ajax.pm


```
get '/' => sub {
    template 'index';
};
```
{% embed include file="src/examples/snippets/1/lib/D2/Ajax.pm" %}

* http://127.0.0.1:5000/api/v1/greeting
* curl http://127.0.0.1:5000/api/v1/greeting


```
{"text":"Hello World"}
```


* curl -I http://127.0.0.1:5000/api/v1/greeting


```
HTTP/1.0 200 OK
Date: Mon, 24 Aug 2015 14:21:11 GMT
Server: HTTP::Server::PSGI
Server: Perl Dancer2 0.161000
Content-Type: application/json
Content-Length: 22
```




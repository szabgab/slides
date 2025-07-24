# HTTP Server


{% embed include file="src/examples/http/http-server.js" %}

```
$ curl http://localhost:8000
Hello World

$ curl -i http://localhost:8000
HTTP/1.1 200 OK
content-type: text/plain
Date: Thu, 30 Jan 2014 21:03:36 GMT
Connection: keep-alive
Transfer-Encoding: chunked

Hello World
```

Point out the Connection: keep-alive   - in modern web you can send several requsts on the same connection
Transfer-Encoding: chunked   - streaming



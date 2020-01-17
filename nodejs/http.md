# HTTP
{id: http}

## HTTP Hello World
{id: http-hello-world}
{i: http}
{i: createServer}
{i: listen}

![](examples/http/http_hello_world.js)


## HTTP Return JSON
{id: http-return-json}
{i: writeHead}
{i: Content-type}

![](examples/http/http_return_json.js)


## HTTP Server
{id: http-server}

![](examples/http/http-server.js)

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


## Transfer-Encoding: chunked
{id: chunked}

![](examples/http/http-server2.js)

In this example, if we fetch it with curl, we'll see the Hello arrives first and then after 2 seconds world arrives.
This is what has been provided by the chunked parameter. This script might fetch some data from a database or from some
other source. Instead of building up the whole response in the server and then sening it out only when it is ready,
we send it out in chunks as parts of it got ready.

If there was a  Content-Length the client could know when the data ends, but with chunked budy it has to
use the http://en.wikipedia.org/wiki/Chunked_transfer_encoding  which basically means, when a chunk of size 0 arrives
that's the end of the current document.

Apache bench: ab -n 100 -c 100 http://127.0.0.1:8000/

## Mashup
{id: mashup}

While one process is still "running" and printing "world" every 5 seconds, we add a new "process"
fetching a website every 2 seconds. It just works.

![](examples/http/mash.js)



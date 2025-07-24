# Transfer-Encoding: chunked

{% embed include file="src/examples/http/http-server2.js" %}

In this example, if we fetch it with curl, we'll see the Hello arrives first and then after 2 seconds world arrives.
This is what has been provided by the chunked parameter. This script might fetch some data from a database or from some
other source. Instead of building up the whole response in the server and then sening it out only when it is ready,
we send it out in chunks as parts of it got ready.

If there was a  Content-Length the client could know when the data ends, but with chunked budy it has to
use the http://en.wikipedia.org/wiki/Chunked_transfer_encoding  which basically means, when a chunk of size 0 arrives
that's the end of the current document.

Apache bench: ab -n 100 -c 100 http://127.0.0.1:8000/



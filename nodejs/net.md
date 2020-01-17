# Net
{id: net}

## The net module
{id: net-module}

* [net](https://nodejs.org/api/net.html)


## TCP Server
{id: tcp-server}

![](examples/net/tcp-server.js)

node examples/net/tcp-server.js


```
$ telnet localhost 8000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
hello
world
Connection closed by foreign host.
```

## TCP Echo Server
{id: tcp-echo-server}

![](examples/net/tcp-server-echo.js)

## Chat server
{id: chat-server}

![](examples/net/chat.js)

This works, but when someone disconnects, the dead socket remains in the array and when we try to write to it it will blow up.

## Remove dead sockets
{id: remove-dead-sockets}

```
    socket.on('end', function() {
        var i = sockets.indexOf(socket);
        sockets.splice(i, 1)
    });
```

![](examples/net/chat2.js)


## Stop echoing
{id: stop-echoing}

```
        if (sockets[i] == socket) continue;
```

![](examples/net/chat3.js)



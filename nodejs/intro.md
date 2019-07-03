# NodeJS
{id: index}

## Self introduction
{id: self-introduction}

* [Gábor Szabó](https://www.linkedin.com/in/szabgab/) @szabgab
* Help organizations generate value faster in a sustainable way.
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)


## What is NodeJS ?
{id: what-is-nodejs}

* Node is a runtime environment for executing JavaScript code
* Non-blocking (asynchronous) architecture
* It has an event loop with event queue
* It is good for network-intensive apps, but not good for CPU intensive applications
* Running on top of the V8 Virtual Machine written by Google, which is also the JavaScript engine in Chrome.

## Installation
{id: installation}

* [NodeJS](http://nodejs.org/)  pick the LTS

```
whet https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz
tar xf ~/Downloads/node-v10.16.0-linux-x64.tar.xz
sudo mv node-v10.16.0-linux-x64/ /opt
sudo chown -R root.root /opt/node-v10.16.0-linux-x64/

export PATH=$PATH:/opt/node-v10.16.0-linux-x64/bin
```

## NodeJS version
{id: check-nodejs-version}

```
$ which node
/opt/node-v10.16.0-linux-x64/bin/node

$ node -v
v10.16.0

```

## Hello World
{id: hello-world}


![](examples/hello_world.js)

```
$ node examples/hello_world.js
Hello World
```

## Hello World with sh
{id: hello-world-sh}

![](examples/hello_world_sh.js)

Make it executable:

```
chmod +x examples/hello_world_sh.js
```

Run it directly

```
./examples/hello_world_sh.js
```

## Hello World in function
{id: hello-world-in-function}

![](examples/hello_world_function.js)


## Parameter passing to function
{id: parameter-passing-to-function}

![](examples/hello_person.js)

## Command line arguments (argv)
{id: command-line-arguments-foreach}

[](https://nodejs.org/docs/latest/api/process.html#process_process_argv)o

![](examples/argv_foreach.js)

## Command line arguments (argv)
{id: command-line-arguments}

![](examples/argv.js)

```
node examples/argv.js "hello world"
3
hello world
```

## setTimeout
{id: set-timeout}

![](examples/with_timeout.js)

```
$ node examples/with_timeout.js
hello
world
```

## setInterval
{id: set-interval}

![](examples/with_interval.js)

```
$ node examples/with_interval.js
hello
world
world
world
^C
```

## Template literals (template strings)
{id: template-literals}

* Using backtick!
* In ES2015/ES6

![](examples/template_literals.js)

```
$ node examples/template_literals.js
Hello Kate
```

## Create library
{id: create-library}

![](examples/lib.js)

![](examples/app.js)

```
$ node examples/app.js
Loading module
Hello World
Hello Foo
```

It is better to define as constant so we won't change it by mistake


## Function as a Library
{id: function-as-a-library}

From a module we can export a module or a single function like this:
// module.exports = hi;

![](examples/lib2.js)

![](examples/app2.js)

## What is in a module?
{id: what-is-in-a-module}

![](examples/my_module.js)

## OS module
{id: os-module}

* A bunch of OS-related methods
* [os](https://nodejs.org/api/os.html)

![](examples/the_os_module.js)


## Read directory sync
{id: read-directory-sync}

![](examples/readdir_sync.js)

## Read directory async
{id: read-directory-async}

![](examples/readdir_async.js)


## Exception
{id: exception}

```
throw new Error("a problem, we have");
```


## REPL
{id: repl}

```
node
>
...
Ctrl-d
```


## npm
{id: npm}

* [npm](https://www.npmjs.com/)

## Express
{id: express}

```
npm install express
```

## npx
{id: npx}

[](https://www.npmjs.com/package/npx)

https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b


## Other
{id: other}

Because node.js does not live in the browser it does not have the DOM. But it has a main object called <b>process</b> and you can ask for <b>process.pid</b>

Node exists when it has nothing more to do. It reference counts the callbacks and when that goes to 0 it exits.

We can use global.console.log() or console.log()

clearTimeout()
clearInterval

var message = '';


[A TAP test framework for Node.js](https://github.com/isaacs/node-tap)

## Resources
{id: resources}

* [Ryan Dahl (author of node.js)](http://www.youtube.com/watch?v=jo_B4LTHi3I)
* [How do I get started with Node.JS](https://stackoverflow.com/questions/2353818/how-do-i-get-started-with-node-js)
* [](https://www.youtube.com/watch?v=TlB_eWDSMt4)
* [](https://www.youtube.com/watch?v=RLtyhwFtXQA)
* [](http://www.nodebeginner.org/)


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


## TCP Server
{id: tcp-server}

![](examples/http/tcp-server.js)

node examples/basics/tcp-server.js


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

![](examples/http/tcp-server-echo.js)

## Chat server
{id: chat-server}

![](examples/http/chat.js)

This works, but when someone disconnects, the dead socket remains in the array and when we try to write to it it will blow up.

## Remove dead sockets
{id: remove-dead-sockets}

```
    socket.on('end', function() {
        var i = sockets.indexOf(socket);
        sockets.splice(i, 1)
    });
```

![](examples/http/chat2.js)


## Stop echoing
{id: stop-echoing}

```
        if (sockets[i] == socket) continue;
```

![](examples/http/chat3.js)



## Debugging
{id: debugging}

Add "debugger;" to the code. That will set a breakpoint if running under the debugger.
node debug code.js
debug> help

debug> quit

* [Node inspector](https://github.com/node-inspector/node-inspector)
* Eclipse plugin

## Mashup
{id: mashup}

While one process is still "running" and printing "world" every 5 seconds, we add a new "process"
fetching a website every 2 seconds. It just works.

![](examples/http/mash.js)


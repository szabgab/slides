# NodeJS basic
{id: nodejs-index}

## What is NodeJS ?
{id: what-is-nodejs}

* Node is a runtime environment for executing JavaScript code.
* Non-blocking (asynchronous) architecture.
* It has an event loop with event queue.
* It is good for network-intensive apps, but not good for CPU intensive applications.
* Running on top of the V8 Virtual Machine written by Google, which is also the JavaScript engine in Chrome.

## NodeJS Installation
{id: installation}

* [NodeJS](http://nodejs.org/)  pick the LTS

## NodeJS Installation Linux
{id: installation-linux}

By the time you are reading this, there might have a newer LTS version already.

```
export NODEJS=v12.14.1
wget https://nodejs.org/dist/$NODEJS/node-$NODEJS-linux-x64.tar.xz
tar xf node-$NODEJS-linux-x64.tar.xz
sudo mv node-$NODEJS-linux-x64/ /opt
sudo chown -R root.root /opt/node-$NODEJS-linux-x64/
```

Add it to the PATH:

```
echo "export PATH=\$PATH:/opt/node-$NODEJS-linux-x64/bin" >> ~/.bashrc
```

## NodeJS version
{id: check-nodejs-version}
{i: node}

```
$ which node
/opt/node-v12.14.1-linux-x64/bin/node

$ node -v
v12.14.1
```

## Hello World
{id: hello-world}
{i: console}
{i: log}

![](examples/node-intro/hello_world.js)

```
$ node examples/node-intro/hello_world.js
```

![](examples/node-intro/hello_world.out)

## Hello World with sh
{id: hello-world-sh}

![](examples/node-intro/hello_world_sh.js)

Make it executable:

```
chmod +x examples/node-intro/hello_world_sh.js
```

Run it directly

```
./examples/node-intro/hello_world_sh.js
```

## Hello World in function
{id: hello-world-in-function}
{i: function}

![](examples/node-intro/hello_world_function.js)
![](examples/node-intro/hello_world_function.out)


## Parameter passing to function
{id: parameter-passing-to-function}

![](examples/node-intro/hello_person.js)
![](examples/node-intro/hello_person.out)

## Command line arguments (argv)
{id: command-line-arguments}
{i: process}
{i: argv}

Throught the [process](https://nodejs.org/api/process.html) object we can access the command line of our program.
The first value is `node` itself. The second value is our code, then come the values from that the user supplied.

![](examples/node-intro/argv.js)

```
$ node argv.js "hello world" Foo
```

```
4
[
  '/opt/node-v12.14.1-linux-x64/bin/node',
  '/home/gabor/work/slides/nodejs/examples/node-intro/argv.js',
  'hello world',
  'Foo'
]

/opt/node-v12.14.1-linux-x64/bin/node
/home/gabor/work/slides/nodejs/examples/node-intro/argv.js
hello world
Foo
undefined
```

## Command line arguments - forEach (argv)
{id: command-line-arguments-foreach}
{i: forEach}

[argv](https://nodejs.org/docs/latest/api/process.html#process_process_argv)

Try: `node argv_foreach.js Hello my world`

![](examples/node-intro/argv_foreach.js)
![](examples/node-intro/argv_foreach.out)

## Define function with arrow notation
{id: define-function-with-arrow-notation}

![](examples/node-intro/add.js)
![](examples/node-intro/add.out)

## setTimeout
{id: set-timeout}
{i: setTimeout}

Delayed execution, callback function.

* First we use `setTimeout` to schedule an anonymous function to be executed 1000 ms later.
* Then we print "hello" to the console.
* Then, after a second, the functions starts running and prints "world"

![](examples/node-intro/with_timeout.js)

```
$ node examples/node-intro/with_timeout.js
hello
world
```

## setInterval
{id: set-interval}
{i: setInterval}

* `setInterval` allows for repeated calls. We can stop this infinite calling using Ctrl-C.

![](examples/node-intro/with_interval.js)

```
$ node examples/node-intro/with_interval.js
hello
world
world
world
^C
```

## clearInterval
{id: clear-interval}
{i: clearInterval}
{i: setInterval}
{i: setTimeout}

* `setInterval` returns an identifier that can later be used to stop the scheduled process.
* `clearInterval` will stop a scheduled process.

![](examples/node-intro/with_clearinterval.js)

```
$ node examples/node-intro/with_clearinterval.js
```

![](examples/node-intro/with_clearinterval.out)

## Template literals (template strings)
{id: template-literals}

* Using backtick!
* In ES2015/ES6

![](examples/node-intro/template_literals.js)

```
$ node examples/node-intro/template_literals.js
Hello Kate
```

## constant (const)
{id: constants}

![](examples/node-intro/const.js)

```
$ node examples/node-intro/const.js
3.14
/home/gabor/work/slides/nodejs/examples/node-intro/const.js:6
pi = 3.15;
   ^

TypeError: Assignment to constant variable.
    at Object.<anonymous> (/home/gabor/work/slides/nodejs/examples/node-intro/const.js:6:4)
    at Module._compile (internal/modules/cjs/loader.js:776:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:787:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:829:12)
    at startup (internal/bootstrap/node.js:283:19)
    at bootstrapNodeJSCore (internal/bootstrap/node.js:622:3)
```

## var
{id: var}

![](examples/node-intro/var1.js)

![](examples/node-intro/var2.js)

![](examples/node-intro/var3.js)

## let
{id: let}

![](examples/node-intro/let1.js)

![](examples/node-intro/let2.js)

## var let
{id: var-let}

![](examples/node-intro/var_let.js)

## let var
{id: let-var}

![](examples/node-intro/let_var.js)


## Create library
{id: create-library}

![](examples/node-intro/lib.js)

![](examples/node-intro/app.js)

```
$ node examples/node-intro/app.js
Loading module
Hello World
Hello Foo
```

It is better to define as constant so we won't change it by mistake


## Function as a Library
{id: function-as-a-library}

From a module we can export a module or a single function like this:
// module.exports = hi;

![](examples/node-intro/lib2.js)

![](examples/node-intro/app2.js)

## What is in a module?
{id: what-is-in-a-module}

![](examples/node-intro/my_module.js)

## OS module
{id: os-module}

* A bunch of OS-related methods
* [os](https://nodejs.org/api/os.html)

![](examples/node-intro/the_os_module.js)


## File-system related operations (fs)
{id: file-system-related-operations}

[fs](https://nodejs.org/docs/latest/api/fs.html)

## Read file
{id: read-file}

![](examples/node-intro/read_file.js)

## Write file
{id: write-file}

![](examples/node-intro/write_file.js)

## Append to file
{id: append-to-file}

![](examples/node-intro/append_to_file.js)

## Delete file (unlink file)
{id: delete-file}

![](examples/node-intro/delete_file.js)

## Read (and write) file by chunks
{id: read-write-file-by-chunks}

![](examples/node-intro/read_write_by_chunks.js)

## Read (and write) file by chunks using pipe
{id: read-write-file-by-pipe}

![](examples/node-intro/read_write.js)


## Create a directory (folder) (mkdir)
{id: create-directory}

![](examples/node-intro/create_directory.js)

## Remove a directory (folder) (rmdir)
{id: remove-directory}

![](examples/node-intro/remove_directory.js)


## Read directory sync (readdirSync)
{id: read-directory-sync}

![](examples/node-intro/readdir_sync.js)

## Read directory async (readdir)
{id: read-directory-async}

![](examples/node-intro/readdir_async.js)

## Read directory async error handline
{id: read-directory-async-errors}

![](examples/node-intro/readdir_async_errors.js)

## Rename a file (rename)
{id: rename-file}

fs.rename(from, to, (err) => {})

![](examples/node-intro/rename_file.js)


## The path related tools
{id: path-related-tools}

* [path](https://nodejs.org/docs/latest/api/path.html)

## Path to the current file
{id: path-to-current-file}

![](examples/node-intro/path_to_file.js)

## Relative path inside a project
{id: relative-path-inside-a-project}


```
project_dir/
   /bin/
       code.js
   /templates
       main.html
```

![](examples/node-intro/relative_path.js)

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



## Other
{id: other}

Because node.js does not live in the browser it does not have the DOM. But it has a main object called <b>process</b> and you can ask for <b>process.pid</b>

Node exists when it has nothing more to do. It reference counts the callbacks and when that goes to 0 it exits.

We can use global.console.log() or console.log()

clearTimeout()
clearInterval

var message = '';


[A TAP test framework for Node.js](https://github.com/isaacs/node-tap)

## Class
{id: class}

![](examples/node-intro/myclass.js)

## HTTP Hello World
{id: http-hello-world}

![](examples/node-intro/http_hello_world.js)


## HTTP Return JSON
{id: http-return-json}

![](examples/node-intro/http_return_json.js)


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

## Resources
{id: resources}

* [Ryan Dahl (author of node.js)](http://www.youtube.com/watch?v=jo_B4LTHi3I)
* [How do I get started with Node.JS](https://stackoverflow.com/questions/2353818/how-do-i-get-started-with-node-js)
* [](https://www.youtube.com/watch?v=TlB_eWDSMt4)
* [](https://www.youtube.com/watch?v=RLtyhwFtXQA)
* [](http://www.nodebeginner.org/)
* [](https://www.youtube.com/watch?v=TlB_eWDSMt4)
* [](https://www.youtube.com/watch?v=RLtyhwFtXQA)





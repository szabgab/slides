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

* http://nodejs.org/  pick the LTS

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

## Other
{id: other}

Because node.js does not live in the browser it does not have the DOM. But it has a main object called <b>process</b> and you can ask for <b>process.pid</b>

Node exists when it has nothing more to do. It reference counts the callbacks and when that goes to 0 it exits.

## Resources
{id: resources}

* [Ryan Dahl (author of node.js)](http://www.youtube.com/watch?v=jo_B4LTHi3I)
* [How do I get started with Node.JS](https://stackoverflow.com/questions/2353818/how-do-i-get-started-with-node-js)
* [](https://www.youtube.com/watch?v=TlB_eWDSMt4)
* [](https://www.youtube.com/watch?v=RLtyhwFtXQA)



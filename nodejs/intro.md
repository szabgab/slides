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

## Resources
{id: resources}

* [Ryan Dahl (author of node.js)](http://www.youtube.com/watch?v=jo_B4LTHi3I)
* [How do I get started with Node.JS](https://stackoverflow.com/questions/2353818/how-do-i-get-started-with-node-js)
* [](https://www.youtube.com/watch?v=TlB_eWDSMt4)
* [](https://www.youtube.com/watch?v=RLtyhwFtXQA)



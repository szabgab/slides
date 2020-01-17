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

## Variables with let
{id: variables-with-let}




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

## clearTimeout
{id: clear-timeout}
{i: clearTimeout}

![](examples/node-intro/clear_timeout.js)
![](examples/node-intro/clear_timeout.out)

## Template literals (template strings) - variable interpolation
{id: template-literals}

![](examples/node-intro/template_literals.js)

```
$ node examples/node-intro/template_literals.js
```

![](examples/node-intro/template_literals.out)

## constant (const)
{id: constants}
{i: const}

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
{i: var}

![](examples/node-intro/var1.js)

![](examples/node-intro/var2.js)

![](examples/node-intro/var3.js)

## let
{id: let}
{i: let}

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
{i: require}

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
{i: module}

* The `module` object represents the current module
* See more about [modules](https://nodejs.org/api/modules.html)

![](examples/node-intro/my_module.js)

## OS module
{id: os-module}
{i: os}
{i: totalmem}
{i: freemem}
{i: uptime}
{i: loadavg}
{i: platform}
{i: hostname}
{i: type}
{i: tmpdir}
{i: networkInterfaces}

* A bunch of OS-related methods
* [os](https://nodejs.org/api/os.html)

![](examples/node-intro/the_os_module.js)


## The path related tools
{id: path-related-tools}

* [path](https://nodejs.org/docs/latest/api/path.html)

## Path to the current file
{id: path-to-current-file}
{i: __filename}
{i: __dirname}

![](examples/node-intro/path_to_file.js)

## Relative path inside a project
{id: relative-path-inside-a-project}
{i: path}
{i: dirname}
{i: join}


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
{i: throw}
{i: Error}

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

## Debugging
{id: debugging}

Add "debugger;" to the code. That will set a breakpoint if running under the debugger.
node debug code.js
debug> help

debug> quit

* [Node inspector](https://github.com/node-inspector/node-inspector)
* Eclipse plugin

## for loop
{id: for-loop}
{i: for}

![](examples/node-intro/for_loop.js)
![](examples/node-intro/for_loop.out)



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
export NODEJS=v14.15.1
wget https://nodejs.org/dist/$NODEJS/node-$NODEJS-linux-x64.tar.xz 
tar xf node-$NODEJS-linux-x64.tar.xz
sudo mv node-$NODEJS-linux-x64/ /opt
sudo chown -R root.root /opt/node-$NODEJS-linux-x64/
sudo ln -s /opt/node-$NODEJS-linux-x64 /opt/node
```

Add it to the PATH:

```
echo "export PATH=\$PATH:/opt/node/bin" >> ~/.bashrc
```

## NodeJS version
{id: check-nodejs-version}
{i: node}

```
$ which node
/opt/node/bin/node

$ node -v
v14.15.1
```

## Hello World
{id: hello-world}
{i: console}
{i: log}

![](examples/basic/hello_world.js)

```
$ node examples/basic/hello_world.js
```

![](examples/basic/hello_world.out)

## Comments
{id: comments}
{i: //}


![](examples/basic/comments.js)
![](examples/basic/comments.out)


## Exercise: Hello World
{id: exercis-hello-world}

* The primary goal of this exercise is to make sure you have your environment ready to write more code.
* Create a file called `hello.js` and make it print "Hello World".
* Run the code from the command line.
* Run the code from your IDE, if you use one.
* Add some comments to your code and check if you can still run it.


## Hello World with sh
{id: hello-world-sh}

Unix-specific issue:

![](examples/basic/hello_world_sh.js)

Make the file executable:

```
chmod +x examples/basic/hello_world_sh.js
```

Run it directly

```
./examples/basic/hello_world_sh.js
```

## Literal Values and types
{id: literal-values}
{i: typeof}
{i: number}
{i: string}
{i: boolean}


![](examples/basic/values.js)


## Declare variables with let
{id: variables-with-let}
{i: let}

![](examples/basic/add.js)

## Hello World in function
{id: hello-world-in-function}
{i: function}

![](examples/basic/hello_world_function.js)
![](examples/basic/hello_world_function.out)


## Parameter passing to function
{id: parameter-passing-to-function}

![](examples/basic/hello_person.js)
![](examples/basic/hello_person.out)

## for loop
{id: for-loop}
{i: for}

![](examples/basic/for_loop.js)
![](examples/basic/for_loop.out)

## Array
{id: array}

![](examples/basic/array.js)

## Command line arguments (argv)
{id: command-line-arguments}
{i: process}
{i: argv}

Throught the [process](https://nodejs.org/api/process.html) object we can access the command line of our program.
The first value is `node` itself. The second value is our code, then come the values from that the user supplied.

![](examples/basic/argv.js)

```
$ node argv.js "hello world" Foo
```

```
4
[
  '/opt/node-v12.14.1-linux-x64/bin/node',
  '/home/gabor/work/slides/nodejs/examples/basic/argv.js',
  'hello world',
  'Foo'
]

/opt/node-v12.14.1-linux-x64/bin/node
/home/gabor/work/slides/nodejs/examples/basic/argv.js
hello world
Foo
undefined
```

## Command line arguments - forEach (argv)
{id: command-line-arguments-foreach}
{i: forEach}

[argv](https://nodejs.org/docs/latest/api/process.html#process_process_argv)

Try: `node argv_foreach.js Hello my world`

![](examples/basic/argv_foreach.js)
![](examples/basic/argv_foreach.out)

## Define function with arrow notation
{id: define-function-with-arrow-notation}

![](examples/basic/add_function.js)
![](examples/basic/add_function.out)

## setTimeout - delayed execution
{id: set-timeout}
{i: setTimeout}

Delayed execution, callback function.

* First we use `setTimeout` to schedule an anonymous function to be executed 1000 ms later.
* Then we print "hello" to the console.
* Then, after a second, the functions starts running and prints "world"

![](examples/basic/with_timeout.js)

```
$ node examples/basic/with_timeout.js
hello
world
```

## setInterval - scheduled execution
{id: set-interval}
{i: setInterval}

* `setInterval` allows for repeated calls. We can stop this infinite calling using Ctrl-C.

![](examples/basic/with_interval.js)

```
$ node examples/basic/with_interval.js
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

![](examples/basic/with_clearinterval.js)

```
$ node examples/basic/with_clearinterval.js
```

![](examples/basic/with_clearinterval.out)

## clearTimeout
{id: clear-timeout}
{i: clearTimeout}

![](examples/basic/clear_timeout.js)
![](examples/basic/clear_timeout.out)

## Template literals (template strings) - variable interpolation
{id: template-literals}

![](examples/basic/template_literals.js)

```
$ node examples/basic/template_literals.js
```

![](examples/basic/template_literals.out)


## Scope of variables and constants
{id: variables}
{i: let}
{i: var}
{i: const}

There are several ways to start declaring and using variables and constants.
In general the best is to use the `let` keyword.

![](examples/basic/variables.js)


## constant (const)
{id: constants}
{i: const}

![](examples/basic/const.js)

```
$ node examples/basic/const.js
3.14
/home/gabor/work/slides/nodejs/examples/basic/const.js:6
pi = 3.15;
   ^

TypeError: Assignment to constant variable.
    at Object.<anonymous> (/home/gabor/work/slides/nodejs/examples/basic/const.js:6:4)
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

![](examples/basic/var1.js)

![](examples/basic/var2.js)

![](examples/basic/var3.js)

## let
{id: let}
{i: let}

![](examples/basic/let1.js)

![](examples/basic/let2.js)

## var let
{id: var-let}

![](examples/basic/var_let.js)

## let var
{id: let-var}

![](examples/basic/let_var.js)


## Create library
{id: create-library}
{i: require}

![](examples/basic/lib.js)

![](examples/basic/app.js)

```
$ node examples/basic/app.js

Loading module
Hello World
Hello Foo
```

It is better to define as constant so we won't change it by mistake


## Function as a Library
{id: function-as-a-library}

From a module we can export a module or a single function like this:
// module.exports = hi;

![](examples/basic/lib2.js)

![](examples/basic/app2.js)

```
$ node examples/basic/app2.js

Loading module
Hello World
Hello Foo
```

## Loading a library twice
{id: loading-a-library}

* Loads it only once but allows access to it from several names.

![](examples/basic/app22.js)

```
$ node examples/basic/app22.js

Loading module
Hello World
Hello Foo
Hello Bar
```


## What is in a module?
{id: what-is-in-a-module}
{i: module}

* The `module` object represents the current module
* See more about [modules](https://nodejs.org/api/modules.html)

![](examples/basic/my_module.js)

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

![](examples/basic/the_os_module.js)


## The path related tools
{id: path-related-tools}

* [path](https://nodejs.org/docs/latest/api/path.html)

## Path to the current file
{id: path-to-current-file}
{i: __filename}
{i: __dirname}

![](examples/basic/path_to_file.js)

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

![](examples/basic/relative_path.js)

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


## Callback
{id: callback}

![](examples/basic/callback.js)


## Closure
{id: closure}

![](examples/basic/closure.js)



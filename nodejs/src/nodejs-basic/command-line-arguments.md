# Command line arguments (argv)

* process
* argv

Throught the [process](https://nodejs.org/api/process.html) object we can access the command line of our program.
The first value is `node` itself. The second value is our code, then come the values from that the user supplied.

{% embed include file="src/examples/basic/argv.js" %}

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



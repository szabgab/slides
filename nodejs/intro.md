# NodeJS
{id: index}

## Self introduction
{id: self-introduction}

* [Gábor Szabó](https://www.linkedin.com/in/szabgab/) @szabgab
* Help organizations generate value faster in a sustainable way.
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)


## Installation
{id: installation}

* http://nodejs.org/  pick the LTS

Node is set of library running on top of the V8 Virtual Machine written by Google, which is also the JavaScript engine in Chrome.


```
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


## setTimeout
{id: set-timeout}

[](examples/with_timeout.js)

```
$ node examples/with_timeout.js
hello
world
```

## setInterval
{id: set-interval}

[](examples/with_interval.js)

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



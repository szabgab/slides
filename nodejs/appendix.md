# Appendix
{id: appendix}

## Other
{id: other}

Because node.js does not live in the browser it does not have the DOM. But it has a main object called `process` and you can ask for `process.pid`.

Node exits when it has nothing more to do. It reference counts the callbacks and when that goes to 0 it exits.

We can use global.console.log() or console.log()

[A TAP test framework for Node.js](https://github.com/isaacs/node-tap)


## Resources
{id: resources}

* [Ryan Dahl (author of node.js)](http://www.youtube.com/watch?v=jo_B4LTHi3I)
* [How do I get started with Node.JS](https://stackoverflow.com/questions/2353818/how-do-i-get-started-with-node-js)
* [Node.js Tutorial for Beginners: Learn Node in 1 Hour | Mosh](https://www.youtube.com/watch?v=TlB_eWDSMt4)
* [Learn Node.js - Full Tutorial for Beginners](https://www.youtube.com/watch?v=RLtyhwFtXQA)
* [The Node Beginner Book](http://www.nodebeginner.org/)

## request
{id: request}

* [request](https://www.npmjs.com/package/request)
* It is deprecated, use [http](https://nodejs.org/api/http.html) instead

```
npm install request
node http_request.js
```

![](examples/networking/http_request.js)

## http client
{id: http-client}

* [http](https://nodejs.org/api/http.html)

![](examples/networking/http_agent.js)

```
node http_agent.js
```

## ping
{id: ping}

* [net-ping](https://www.npmjs.com/package/net-ping)

![](examples/networking/ping_demo.js)

```
npm install net-ping
sudo /opt/node/bin/node ping_demo.js
```


## Telnet server
{id: telnet-server}

* [telnet](https://www.npmjs.com/package/telnet)

![](examples/networking/telnet_server.js)


# Other


Because node.js does not live in the browser it does not have the DOM. But it has a main object called `process` and you can ask for `process.pid`.

Node exits when it has nothing more to do. It reference counts the callbacks and when that goes to 0 it exits.

We can use global.console.log() or console.log()

[A TAP test framework for Node.js](https://github.com/isaacs/node-tap)



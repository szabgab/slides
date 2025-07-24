# setTimeout - delayed execution

* setTimeout

Delayed execution, callback function.

* First we use `setTimeout` to schedule an anonymous function to be executed 1000 ms later.
* Then we print "hello" to the console.
* Then, after a second, the functions starts running and prints "world"

{% embed include file="src/examples/basic/with_timeout.js" %}

```
$ node examples/basic/with_timeout.js
hello
world
```



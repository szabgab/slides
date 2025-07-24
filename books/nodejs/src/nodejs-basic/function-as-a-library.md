# Function as a Library


From a module we can export a module or a single function like this:
// module.exports = hi;

{% embed include file="src/examples/basic/lib2.js" %}

{% embed include file="src/examples/basic/app2.js" %}

```
$ node examples/basic/app2.js

Loading module
Hello World
Hello Foo
```



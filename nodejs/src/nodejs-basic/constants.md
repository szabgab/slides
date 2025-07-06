# constant (const)

* const

{% embed include file="src/examples/basic/const.js" %}

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



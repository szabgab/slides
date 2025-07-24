# Bad Comments in JavaScript

It is better to avoid the multiline comments /*  */
Especially as most editors support the commenting out of a whole
section of lines with just one keystroke.


{% embed include file="src/examples/js/bad_comments.js" %}

```
SyntaxError: unterminated string literal
```

```
.../examples/js/bad_comments.js:8
   console.log("/* hello */")
                           ^^
SyntaxError: Unexpected token ILLEGAL
    at exports.runInThisContext (vm.js:73:16)
    at Module._compile (module.js:443:25)
    at Object.Module._extensions..js (module.js:478:10)
    at Module.load (module.js:355:32)
    at Function.Module._load (module.js:310:12)
    at Function.Module.runMain (module.js:501:10)
    at startup (node.js:129:16)
    at node.js:814:3
```




# JSON parsing NaN, Infinite, and null (Node.js" %}

{% embed include file="src/examples/js/json_parse_nan.js" %}

```
{ v: 42 }
{ n: null }
undefined:1
{ "x" : NaN }
        ^
SyntaxError: Unexpected token N
```





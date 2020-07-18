# Advanced JavaScript
{id: advanced-javascript}

## Stringify NaN, Infinite, and null
{id: stringify-nan-infinite-and-null}
{i: NaN}
{i: Infinite}
{i: null}
![](examples/js/stringify_nan.js)

```
{
  "x": null
}
{
  "y": null
}
{
  "z": null
}
{
  "n": null
}
```


## JSON parsing NaN, Infinite, and null
{id: json-parsing-nan-infinite-and-null}
![](examples/js/json_parse_nan.html)

```
Object { v: 42 } json_parse_nan.html:3:0
Object { n: null } json_parse_nan.html:6:0
SyntaxError: JSON.parse: unexpected character at line 1 column 9 of the JSON data
```


## JSON parsing NaN, Infinite, and null (Node.js)
{id: json-parsing-nan-infinite-and-null-node}
![](examples/js/json_parse_nan.js)

```
{ v: 42 }
{ n: null }
undefined:1
{ "x" : NaN }
        ^
SyntaxError: Unexpected token N
```


## typeof
{id: typeof}
{i: typeof}
![](examples/js/typeof.js)


## typeof and null
{id: typeof-null}
![](examples/js/typeof_null.js)


## Delayed (scheduled) execution - setTimeout
{id: set-timeout}
{i: setTimeout}
![](examples/js/set_timeout.js)


## Recurring execution - setInterval
{id: set-interval}
{i: setInterval}
![](examples/js/set_interval.js)


## Stop recurring execution - clearInterval
{id: clear-interval}
{i: clearInterval}
![](examples/js/clear_interval.js)


## Dates
{id: dates}
{i: Date}
![](examples/js/dates.js)



## sort
{id: sort}
{i: sort}
{i: localCompare}
![](examples/js/sort.js)


## sort object
{id: sort-object}
![](examples/js/sort_object.js)


## sort datestrings
{id: sort-datestrings}
![](examples/js/sort_datestrings.js)


## map
{id: map}
{i: map}
![](examples/js/map.js)



## Closures in JavaScript
{id: closure}
![](examples/js/create_incrementer.js)
![](examples/js/create_counter.js)


## Exception handling
{id: exception-handling}
{i: try}
{i: catch}
![](examples/js/exception.js)


## NodeJS: command line arguments
{id: nodejs-command-line-arguments}
{i: argv}
![](examples/js/node_argv.js)

```
$ node examples/js/nodejs_argv.js foo bar
[ 'node',
  '/Users/gabor/work/training/javascript/examples/js/nodejs_argv.js',
  'foo',
  'bar' ]
--------------
node
/Users/gabor/work/training/javascript/examples/js/nodejs_argv.js
foo
bar
```


## NodeJS: prompt on STDIN
{id: nodejs-prompt}
{i: prompt}

```
npm install prompt
```
![](examples/js/node_prompt.js)


## Transliterate
{id: transliterate}

Work in progress...

![](examples/advanced/transliterate.html)
![](examples/advanced/transliterate.js)




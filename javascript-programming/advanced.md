# Advanced JavaScript
{id: advanced-javascript}

## Stringify NaN, Infinite, and null
{id: stringify-nan-infinite-and-null}
{i: NaN}
{i: Infinite}
{i: null}
![](examples/intro/stringify_nan.js)

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
![](examples/intro/json_parse_nan.html)

```
Object { v: 42 } json_parse_nan.html:3:0
Object { n: null } json_parse_nan.html:6:0
SyntaxError: JSON.parse: unexpected character at line 1 column 9 of the JSON data
```


## JSON parsing NaN, Infinite, and null (Node.js)
{id: json-parsing-nan-infinite-and-null-node}
![](examples/intro/json_parse_nan.js)

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
![](examples/intro/typeof.js)


## typeof and null
{id: typeof-null}
![](examples/intro/typeof_null.js)


## Delayed (scheduled) execution - setTimeout
{id: set-timeout}
{i: setTimeout}
![](examples/intro/set_timeout.js)


## Recurring execution - setInterval
{id: set-interval}
{i: setInterval}
![](examples/intro/set_interval.js)


## Stop recurring execution - clearInterval
{id: clear-interval}
{i: clearInterval}
![](examples/intro/clear_interval.js)


## Dates
{id: dates}
{i: Date}
![](examples/intro/dates.js)



## sort
{id: sort}
{i: sort}
{i: localCompare}
![](examples/intro/sort.js)


## sort object
{id: sort-object}
![](examples/intro/sort_object.js)


## sort datestrings
{id: sort-datestrings}
![](examples/intro/sort_datestrings.js)


## map
{id: map}
{i: map}
![](examples/intro/map.js)



## Closures in JavaScript
{id: closure}
![](examples/intro/create_incrementer.js)
![](examples/intro/create_counter.js)


## Exception handling
{id: exception-handling}
{i: try}
{i: catch}
![](examples/intro/exception.js)


## NodeJS: command line arguments
{id: nodejs-command-line-arguments}
{i: argv}
![](examples/intro/node_argv.js)

```
$ node examples/intro/nodejs_argv.js foo bar
[ 'node',
  '/Users/gabor/work/training/javascript/examples/intro/nodejs_argv.js',
  'foo',
  'bar' ]
--------------
node
/Users/gabor/work/training/javascript/examples/intro/nodejs_argv.js
foo
bar
```


## NodeJS: prompt on STDIN
{id: nodejs-prompt}
{i: prompt}

```
npm install prompt
```
![](examples/intro/node_prompt.js)


## Transliterate
{id: transliterate}

Work in progress...

![](examples/advanced/transliterate.html)
![](examples/advanced/transliterate.js)




# Node.js


Download [Node.js](http://nodejs.org/).
Run as `node`. Ctrl-C (twice) to quit.


On Ubuntu I had to install the `nodejs` package and the command is called
`nodejs` as there was already command called node.

On Mac first install [Homebrew](http://mxcl.github.io/homebrew/) and then `brew install node`.


Maybe you'll need to use the Git bash shell...


```
> .help
> .exit

> .break
```

Some JavaScript using the Node.js REPL


Variables and numbers


```
> a = 23
23
> b = 19
19
> a+b
42
```

The behaviour of + depends on the operands. If even one of them is a sting,
+ will concatenate them as string. Use parseInt() to convert a string to an integer.


```
> c = "1"
> a+c
'231'
> a+parseInt(c)
24
```




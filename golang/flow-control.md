# Flow Control
{id: flow-control}

## if-statements
{id: if-statements}

## if, else, else if
{id: if-else-statements}

```
if cond {
}

if cond {
} else {
}


if cond {
} else if cond {
} else {
}
```

[if - short statement (right before the condition)](https://tour.golang.org/flowcontrol/6)

## if with initializer
{id: if-with-initializer}


![](examples/in-init/if_with_initializer.go)


## Comparision Operators
{id: comparision-operators}

* Work for numeric types but not for strings

```
<
>
<=
>=
==
!=
```

## Short circuit
{id: short-circuit}



## switch
{id: switch}
{i: switch}
{i: case}

![](examples/switch/switch.go)


* multiple values in the same case
* tagless switch statement with real comparisions like `x < 23` in the cases, here cases can overlap
* [video](https://youtu.be/YS4e4q9oBaU?t=11404)
* `fallthrough`
* type switch


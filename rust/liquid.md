# liquid templating
{id: liquid}

## Install
{id: install-liquid}

* [liquid crate](https://crates.io/crates/liquid)
* [documentation](https://docs.rs/liquid/)
* [Ruby liquid web site](https://shopify.github.io/liquid/)

```
cargo add liquid
```

This will update the Cargo.toml to include:

```
[dependencies]
liquid = "0.26.4"
```

## Liquid Hello World
{id: liquid-hello-world}

![](examples/liquid-hello-world/Cargo.toml)
![](examples/liquid-hello-world/src/main.rs)
![](examples/liquid-hello-world/out.txt)

## Liquid Hello World with variable
{id: liquid-hello-world-with-variable}

![](examples/liquid-hello-world-variables/Cargo.toml)
![](examples/liquid-hello-world-variables/out.txt)
![](examples/liquid-hello-world-variables/src/main.rs)

## Liquid Hello World read template from file
{id: liquid-hello-world-read-template-from-file}

![](examples/liquid-hello-world-from-file/Cargo.toml)
![](examples/liquid-hello-world-from-file/out.txt)
![](examples/liquid-hello-world-from-file/src/main.rs)
![](examples/liquid-hello-world-from-file/template.txt)

## Liquid flow control: if - else
{id: liquid-flow-control-if-else}

![](examples/liquid-if-else/Cargo.toml)
![](examples/liquid-if-else/src/main.rs)
![](examples/liquid-if-else/out.txt)

## Liquid object
{id: liquid-object}

![](examples/liquid-objects/Cargo.toml)
![](examples/liquid-objects/src/main.rs)
![](examples/liquid-objects/out.txt)

## Liquid for loop passing a vector or an array
{id: liquid-for-loop}

![](examples/liquid-for-loop/Cargo.toml)
![](examples/liquid-for-loop/out.txt)
![](examples/liquid-for-loop/src/main.rs)

## Liquid for loop with if conditions
{id: liquid-for-loop-with-if-conditions}

![](examples/liquid-loop-and-if/Cargo.toml)
![](examples/liquid-loop-and-if/out.txt)
![](examples/liquid-loop-and-if/src/main.rs)

## Liquid with struct
{id: liquid-with-struct}

![](examples/liquid-with-struct/Cargo.toml)
![](examples/liquid-with-struct/src/main.rs)

## Liquid TODO
{id: liquid-todo}

* pass struct
* Control structures (if, else)
* Loops (for)
* Filters
* Include template
* Layout template (embed template)

## Liquid filters on numbers: plus, minus
{id: liquid-filters-numbers}

![](examples/liquid-filters-numbers/Cargo.toml)
![](examples/liquid-filters-numbers/src/main.rs)
![](examples/liquid-filters-numbers/out.txt)

## Liquid filters on strings: upcase, downcase, capitalize
{id: liquid-filters-strings}

![](examples/liquid-filters-strings/Cargo.toml)
![](examples/liquid-filters-strings/src/main.rs)
![](examples/liquid-filters-strings/out.txt)

## Liquid include
{id: liquid-include}

![](examples/liquid-include/Cargo.toml)
![](examples/liquid-include/out.txt)
![](examples/liquid-include/src/main.rs)


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

## Liquid with struct}
{id: liquid-with-struct}

![](examples/liquid-with-struct/Cargo.toml)
![](examples/liquid-with-struct/src/main.rs)

## Liquid TODO
{id: liquid-todo}

* pass struct
* pass vector
* pass array

* Control structures (if, else)
* Loops
* include template
* layout template (embed template)


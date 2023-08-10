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
{i: parse}

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
{i: parse_file}

![](examples/liquid-hello-world-from-file/Cargo.toml)
![](examples/liquid-hello-world-from-file/out.txt)
![](examples/liquid-hello-world-from-file/src/main.rs)
![](examples/liquid-hello-world-from-file/template.txt)

## Liquid flow control: if - else
{id: liquid-flow-control-if-else}
{i: if}
{i: else}
{i: endif}

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
{i: for}
{i: endfor}

![](examples/liquid-for-loop/Cargo.toml)
![](examples/liquid-for-loop/src/main.rs)
![](examples/liquid-for-loop/out.txt)

## Liquid for loop with if conditions
{id: liquid-for-loop-with-if-conditions}
{i: for}
{i: endfor}
{i: if}
{i: endif}

![](examples/liquid-loop-and-if/Cargo.toml)
![](examples/liquid-loop-and-if/src/main.rs)
![](examples/liquid-loop-and-if/out.txt)


## Liquid filters on numbers: plus, minus
{id: liquid-filters-numbers}
{i: plus}
{i: minus}

* Increment or decerement the number by the given number

![](examples/liquid-filters-numbers/Cargo.toml)
![](examples/liquid-filters-numbers/src/main.rs)
![](examples/liquid-filters-numbers/out.txt)

## Liquid filters on strings: upcase, downcase, capitalize
{id: liquid-filters-strings}
{i: upcase}
{i: downcase}
{i: capitalize}

![](examples/liquid-filters-strings/Cargo.toml)
![](examples/liquid-filters-strings/src/main.rs)
![](examples/liquid-filters-strings/out.txt)

## Liquid filters: first, last
{id: liquid-filters-first-last}
{i: first}
{i: last}

first or last
* character in a string
* element in an array, a vector, or a tuple

![](examples/liquid-filters-order/Cargo.toml)
![](examples/liquid-filters-order/src/main.rs)
![](examples/liquid-filters-order/out.txt)


## Liquid
{id: liquid-todo}

* pass integer, string, bool, vector, tuple, struct
* Control structures (if, else)
* Loops (for)
* Filters
* Include template
* Layout template (embed template)

## Liquid include
{id: liquid-include}
{i: include}
{i: partials}

![](examples/liquid-include/Cargo.toml)

![](examples/liquid-include/templates/page.txt)
![](examples/liquid-include/templates/incl/header.txt)

![](examples/liquid-include/src/main.rs)

![](examples/liquid-include/out.txt)

## Liquid assign to variable in template
{id: liquid-assign}
{i: assign}

![](examples/liquid-assign/Cargo.toml)
![](examples/liquid-assign/src/main.rs)

![](examples/liquid-assign/templates/page.txt)
![](examples/liquid-assign/templates/incl/header.txt)

![](examples/liquid-assign/out.txt)

## Liquid include header and footer
{id: liquid-include-header-and-footer}
{i: include}

![](examples/liquid-include-header-footer/Cargo.toml)
![](examples/liquid-include-header-footer/out.txt)
![](examples/liquid-include-header-footer/src/main.rs)
![](examples/liquid-include-header-footer/templates/incl/footer.txt)
![](examples/liquid-include-header-footer/templates/incl/header.txt)
![](examples/liquid-include-header-footer/templates/page.txt)


## Liquid layout (include and capture)
{id: liquid-layout}
{i: include}
{i: capture}

![](examples/liquid-layout/Cargo.toml)
![](examples/liquid-layout/out.txt)
![](examples/liquid-layout/src/main.rs)
![](examples/liquid-layout/templates/layout.txt)
![](examples/liquid-layout/templates/page.txt)


## Liquid with struct
{id: liquid-with-struct}


![](examples/liquid-with-struct/Cargo.toml)
![](examples/liquid-with-struct/src/main.rs)
![](examples/liquid-with-struct/out.html)


## Liquid filter reverse array
{id: liquid-filter-reverse-array}

![](examples/liquid-filter-reverse/Cargo.toml)
![](examples/liquid-filter-reverse/src/main.rs)

## Liquid for loop: limit, offset, reversed
{id: liquid-for-loop-limit-offset-reversed}
{i: limit}
{i: offset}
{i: reversed}

![](examples/liquid-loops/Cargo.toml)
![](examples/liquid-loops/src/main.rs)



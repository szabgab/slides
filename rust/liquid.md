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

![](examples/liquid-hello-world-variables/out.txt)
![](examples/liquid-hello-world-variables/src/main.rs)

## Liquid Hello World read template from file
{id: liquid-hello-world-read-template-from-file}
{i: parse_file}

![](examples/liquid-hello-world-from-file/out.txt)
![](examples/liquid-hello-world-from-file/src/main.rs)
![](examples/liquid-hello-world-from-file/template.txt)

## Liquid flow control: if - else
{id: liquid-flow-control-if-else}
{i: if}
{i: else}
{i: endif}

![](examples/liquid-if-else/src/main.rs)
![](examples/liquid-if-else/out.txt)

## Liquid flow control: else if written as elsif
{id: liquid-flow-control-elsif}

![](examples/liquid-elsif/src/main.rs)
![](examples/liquid-elsif/out.txt)

## Liquid flow control: case/when
{id: liquid-flow-control-case-when}

![](examples/liquid-case-when/src/main.rs)
![](examples/liquid-case-when/out.txt)

## Liquid object
{id: liquid-object}

![](examples/liquid-objects/src/main.rs)
![](examples/liquid-objects/out.txt)

## Liquid for loop passing a vector or an array
{id: liquid-for-loop}
{i: for}
{i: endfor}

![](examples/liquid-for-loop/src/main.rs)
![](examples/liquid-for-loop/out.txt)

## Liquid for loop with if conditions
{id: liquid-for-loop-with-if-conditions}
{i: for}
{i: endfor}
{i: if}
{i: endif}

![](examples/liquid-loop-and-if/src/main.rs)
![](examples/liquid-loop-and-if/out.txt)


## Liquid filters on numbers: plus, minus
{id: liquid-filters-numbers}
{i: plus}
{i: minus}

* Increment or decerement the number by the given number

![](examples/liquid-filters-numbers/src/main.rs)
![](examples/liquid-filters-numbers/out.txt)

## Liquid filters on strings: upcase, downcase, capitalize
{id: liquid-filters-strings}
{i: upcase}
{i: downcase}
{i: capitalize}

![](examples/liquid-filters-strings/src/main.rs)
![](examples/liquid-filters-strings/out.txt)

## Liquid filters: first, last
{id: liquid-filters-first-last}
{i: first}
{i: last}

first or last
* character in a string
* element in an array, a vector, or a tuple

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

![](examples/liquid-include/templates/page.txt)
![](examples/liquid-include/templates/incl/header.txt)

![](examples/liquid-include/src/main.rs)

![](examples/liquid-include/out.txt)

## Liquid assign to variable in template
{id: liquid-assign}
{i: assign}

![](examples/liquid-assign/src/main.rs)

![](examples/liquid-assign/templates/page.txt)
![](examples/liquid-assign/templates/incl/header.txt)

![](examples/liquid-assign/out.txt)

## Liquid include header and footer
{id: liquid-include-header-and-footer}
{i: include}

![](examples/liquid-include-header-footer/out.txt)
![](examples/liquid-include-header-footer/src/main.rs)
![](examples/liquid-include-header-footer/templates/incl/footer.txt)
![](examples/liquid-include-header-footer/templates/incl/header.txt)
![](examples/liquid-include-header-footer/templates/page.txt)


## Liquid layout (include and capture)
{id: liquid-layout}
{i: include}
{i: capture}

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

![](examples/liquid-filter-reverse/src/main.rs)

## Liquid for loop: limit, offset, reversed
{id: liquid-for-loop-limit-offset-reversed}
{i: limit}
{i: offset}
{i: reversed}

![](examples/liquid-loops/src/main.rs)

## Liquid comma between every two elements (forloop.last)
{id: liquid-forloop-last}

* length
* index   (numbers start from 1)
* index0  (numbers start from 0)
* rindex
* rindex0
* first
* last

![](examples/liquid-loop-last/src/main.rs)

## Liquid: create your own filter: reverse a string
{id: liquid-create-your-own-filter-reverse-a-string}

This is using the [liquid-filter-reverse-string](https://crates.io/crates/liquid-filter-reverse-string). Look at its [source code](https://github.com/szabgab/liquid-filter-reverse-string.rs)

![](examples/liquid-filter-reverse-string-use/Cargo.toml)
![](examples/liquid-filter-reverse-string-use/src/main.rs)

## Liquid: create your own filter: commafy
{id: liquid-create-your-own-filter-commafy}

![](examples/liquid-filter-commafy-use/Cargo.toml)
![](examples/liquid-filter-commafy-use/src/main.rs)


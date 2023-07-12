# Handlebars
{id: handlebars}

## Quick start - unregistered template
{id: handlebars-quick-start-unregistered-template}
{i: Handlebars}
{i: render_template}
{i: json}

* [Handlebars](https://crates.io/crates/handlebars) is templating language implemented in Rust. It is based on the ideas of the original [HandlebarsJS](https://handlebarsjs.com/) but it is not 100% compatible.

* We have a very simple template embedded in our Rust code. It has one placeholder `{{name}}`.
* We pass a JSON string to the `render_template` function.

![](examples/handlebars-quick/src/main.rs)

* The generated output looks like this:

![](examples/handlebars-quick/out.html)

![](examples/handlebars-quick/Cargo.toml)

## Quick start - registered template
{id: handlebars-separate-functions}
{i: register_template_string}
{i: render}

* In this example we register a template to make it easier to reuse it and then use it twice.

![](examples/handlebars-separate-functions/src/main.rs)
![](examples/handlebars-separate-functions/out.html)
![](examples/handlebars-separate-functions/Cargo.toml)

##  Handlebars - render to file
{id: handlebars-render-to-file}

* In some cases we would like to save the generated string in a file.

![](examples/handlebars-render-to-file/src/main.rs)
![](examples/handlebars-render-to-file/hello.html)
![](examples/handlebars-render-to-file/Cargo.toml)

##  Handlebars - read template from file
{id: handlebars-read-template-from-file}

* We have a separate function to read the content of the template file.

![](examples/handlebars-template-file/template.html)
![](examples/handlebars-template-file/src/main.rs)
![](examples/handlebars-template-file/hello.html)
![](examples/handlebars-template-file/Cargo.toml)

## Handlebars - show time of generation
{id: handlebars-show-time-of-generation}

![](examples/handlebars-date/src/main.rs)
![](examples/handlebars-date/template.html)
![](examples/handlebars-date/hello.html)

![](examples/handlebars-date/Cargo.toml)

## Handlebars loop (each) on array
{id: handlebars-each}

![](examples/handlebars-loop/template.html)

![](examples/handlebars-loop/hello.html)
![](examples/handlebars-loop/src/main.rs)

![](examples/handlebars-loop/Cargo.toml)


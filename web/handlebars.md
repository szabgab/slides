# Handlebars
{id: handlebars}

## Getting started with Handlebars
{id: getting-started-with-handlebars}

[Handlebars](http://handlebarsjs.com/)

![](examples/handlebars/include.html)


## Handlebars Template
{id: handlebars-template}

```
Hello `{{first_name}}` {{last_name}}
```
![](examples/handlebars/simple_template.html)


## Handlebars process
{id: handlebars-process}
![](examples/handlebars/process_template.js)

jQuery


```
var source   = $('#text-template').html();
```


## Handlebars inject into DOM
{id: handlebars-inject-into-dom}

**Inject HTML into DOM**


Plain JavaScript


```
document.getElementById('result').innerHTML = html;
```

jQuery


```
$("#result").html(html);
```


## Greeting in JavaScript - html
{id: greeting-in-javascript-html}
![](examples/handlebars/pure_js_greeting.html)


## Greeting in JavaScript - js
{id: greeting-in-javascript}
![](examples/handlebars/pure_js_greeting.js)



## Greeting with Habdlebars - html
{id: greeting-with-handlebars-html}
![](examples/handlebars/handlebars_greeting.html)


## Greeting with Habdlebars - js
{id: greeting-with-handlebars}
![](examples/handlebars/handlebars_greeting.js)


## Greeting with Habdlebars and jQuery - html
{id: greeting-with-handlebars-and-jquery-html}
![](examples/handlebars/handlebars_greeting_jquery.html)


## Greeting with Habdlebars and jQuery - js
{id: greeting-with-handlebars-and-jquery}
![](examples/handlebars/handlebars_greeting_jquery.js)


## Handlebars data
{id: handlebars-data}
![](examples/handlebars/handlebars_data.js)


## Handlebars process
{id: handlebars-process-on-document-ready}
![](examples/handlebars/handlebars_process.js)


## Handlebars object and array
{id: handlebars-object}

```
{{title}}
{{address.street}}
{{names.[0]}} - {{names.[1]}}
{{articles.1.title}}
```
![](examples/handlebars/handlebars_object.html)



## Handlebars each
{id: handlebars-each}
{i: each}

```
{{#each articles}}
   ...
{{/each}}
```
![](examples/handlebars/handlebars_each.html)


## Handlebars if
{id: handlebars-if}
{i: if}

```
{{#if desc}}
   {{desc}}
{{else}}
   No description
{{/if}}
```
![](examples/handlebars/handlebars_if.html)


## Handlebars parent context
{id: handlebars-parent-context}

```
{{../../description}}
```
![](examples/handlebars/handlebars_parent_context.html)


## Handlebars static helpers - html
{id: handlebars-helper-static-html}

```
{{greeting}}
```
![](examples/handlebars/handlebars_helper_static.html)


## Handlebars static helpers - js
{id: handlebars-helper-static}
{i: SafeString}
![](examples/handlebars/handlebars_helper_static.js)

Use SafeString here, if you want to make sure HTML tags are NOT escaped by Handlebars



## Handlebars link helper - html
{id: handlebars-helper-link-html}
{i: this}

```
{{link this}}
```
![](examples/handlebars/handlebars_helper_link.html)


## Handlebars link helper
{id: handlebars-helper-link}
![](examples/handlebars/handlebars_helper_link.js)



## Handlebars if_eq - html
{id: handlebars-helper-if-eq-html}
{i: if_eq}
{i: iff}

Works:


```
{{#if name}}
{{/if}}
```

Does not work:


```
{{#if name === 'Foo'}}
{{/if}}
```

So we will implement


```
{{#if_eq name === 'Foo'}}
{{/if_eq}}
```


Error: if_eq doesn't match if

![](examples/handlebars/handlebars_if_eq.html)


## Handlebars if_eq
{id: handlebars-helper-if-eq}
![](examples/handlebars/handlebars_if_eq.js)


## Handlebars conditionals - html
{id: handlebars-helper-conditionals-html}
{i: iff}

```
{{#iff name '===' 'Foo'}}
```

```
{{#iff answer '>' 30}}
```
![](examples/handlebars/handlebars_helper_conditionals.html)


## Handlebars conditionals
{id: handlebars-helper-conditionals}
![](examples/handlebars/handlebars_helper_conditionals.js)



## Handlebars helpers
{id: handlebars-helpers}

* [Helpers](http://assemble.io/helpers/)
* [Helpers Comparision](http://assemble.io/helpers/helpers-comparison.html)



## Page with back and forward buttons (html)
{id: page-with-back-and-forward-buttons-html}

```
```
![](examples/handlebars/pages.html)


## Page with back and forward buttons (js)
{id: page-with-back-and-forward-buttons-js}
{i: window.location.hash}
{i: hashchange}
![](examples/handlebars/pages.js)





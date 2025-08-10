# Handlebars if_eq - html

* if_eq
* iff

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

{% embed include file="src/examples/handlebars/handlebars_if_eq.html" %}



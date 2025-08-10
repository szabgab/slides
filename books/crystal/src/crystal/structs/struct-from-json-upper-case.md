# Struct from JSON - upper case

* We cannot have attributes starting with upper case so we have to convert the field names to lowercase:
* Using [attribute annotation](https://crystal-lang.org/reference/syntax_and_semantics/annotations/index.html)

{% embed include file="src/examples/struct/struct_from_json_upper.cr" %}
{% embed include file="src/examples/struct/struct_from_json_upper.out" %}



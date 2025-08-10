# Monkey patching DateTime::Tiny

```perl
sub DateTime::Tiny::TO_JSON { shift->as_string };
```
{% embed include file="src/examples/snippets/10/prove_monkey.txt" %}

Testing


```perl
like $items1->{items}[0]{date}, qr/^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d$/;
```




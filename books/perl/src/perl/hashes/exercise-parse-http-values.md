# Exercise: Parse HTTP values

```
You get one line like the following:
fname=Foo&amp;lname=Bar&amp;phone=123&amp;email=foo@bar.com

Build a hash table from it so:
print $h{fname};      #  Foo 
print $h{lname};      #  Bar
...

Start with this file:
```
{% embed include file="src/examples/hashes/split_http_skeleton.pl" %}
{% embed include file="src/examples/hashes/split_http.out" %}




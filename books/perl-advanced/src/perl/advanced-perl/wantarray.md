# wantarray

When called within a function it will return undef, true or false
depending on how was the function called.


```
undef  if it was called in a void context like f();
true   if it was called in a list context like @x = f(); or print f();
false  if it was called in scalar context like $x = f(); or if($f()) {...}
```
{% embed include file="src/examples/advanced-perl/wantarray.pl" %}



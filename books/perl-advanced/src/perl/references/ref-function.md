# The ref() function


* ref

```perl
my $name = 'Foo';
ref($name);           # undef
ref(\$name);          # SCALAR
my $array_ref = [];
ref($array_ref);      # ARRAY
my $hash_ref = {};
ref($hash_ref);       # HASH
my $sub_ref = sub {};
ref($sub_ref);        # CODE
```



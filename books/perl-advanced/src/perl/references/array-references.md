# Array References


* \@array
* ARRAY


To solve the problem we will use references.
Prefixing the array with a back-slash \ creates
a reference to it.


```
my $names_ref  = \@names;
```

```
print $names_ref;      # ARRAY(0x703dcf2)
```

```
@$names_ref
```

but it will be probably more readable to write

```
@{$names_ref}
```

or even

```
@{ $names_ref }
```

Once we know all this we can pass a reference to a function,
within the function we can dereference the array and we
get back the original array.


{% embed include file="src/examples/references/array_references.pl" %}



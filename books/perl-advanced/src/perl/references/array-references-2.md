# Array References

Of course if the arrays are big, copying them is waste of time
and memory. Let's see how can we access the individual elements of
an array when using a reference to that array. Then we won't have
to copy them within the function.


```
my $names_ref = \@names;
```

```
Array      Array Reference
@names     @{ $names_ref }
$names[0]  ${ $names_ref }[0]
           $names_ref->[0]
$#names    $#$names_ref
```

You really don't want to use this `$#$names_ref` among people...



# Hash References

* \%hash
* HASH


Similarly to the Array references one can create references
to Hashes as well.

```
my $phones_ref = \%phones;
```

```
Hash            Hash Reference
%phones         %{ $phones_ref }
$phones{Foo}    ${ $phones_ref }{Foo}
                $phones_ref->{Foo}
keys %phones    keys %{ $phones_ref }
```

Using the print function to print out the content of an Array
was quite OK. Printing a Hash was a disaster. The same happens
once you dereference a reference to an array or hash.


{% embed include file="src/examples/references/hash_reference.pl" %}



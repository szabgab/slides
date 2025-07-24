# Arrays

```
my @people;                           # Declare empty array.
my @names = (                         # Declare array and assign 3 elements.
    'Foo',
    'Bar',
    'Moo',                            # Trailing comma is ok.
);
say $names[0];                        # Access the 0th element 'Foo'
```

```
scalar @names;      # number of elements in the array
$#names;            # the largest index (one less than number of elements)
```

```
push @names, 'Minimacko';
pop @names;
shift @names;
unshift @names, 'Malacka';
```



# References to Array

```
my @names = ('foo', 'bar', 'baz')
my $ref_to_names = \@names;

@names             @$ref_to_names        # de-reference the array

$name[0]           $$ref_to_names[0]
                   $ref_to_names->[0]    # same but looks better

sacalar @names     scalar @$ref_to_names
$#names            $#$ref_to_name        # I never liked this
```



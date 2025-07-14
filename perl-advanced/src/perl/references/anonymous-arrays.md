# Anonymous Arrays

* anonymous array
* []


Occasionally we are not interested in the array @names, just in a reference to it. We can use the scoping trick we saw earlier to force the array out of scope immediately once it was used.

```
my $names_ref;
{
    my @names     = ("Foo", "Bar", "Baz");
    $names_ref = \@names;
}
# @names is not in scope here
# $names_ref is still is
```


We can reach the same result without the temporary array and the
whole scoping issue by creating what we call an "anonymous array".
That is an array that does not have a real name, (@name) just a
reference to it.



```
my $other_names_ref = ["Foo", "Bar", "Baz"];

my $yet_another_names_ref = [ qw(Foo Bar Baz) ];
```


We got used to seeing [] as an indicator of an array element. The same visual
clue will help us remember that the above creates an array reference.


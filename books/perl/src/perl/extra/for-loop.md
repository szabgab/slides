# for loop

* for

```perl
for (INITIALIZE; TEST; INCREMENT) {
    BODY;
}

for (my $i=0; $i &lt; 10; $i++) {
     print "$i\n";
}

# but a foreach loop might be better for the same looping:
foreach my $i (0..9) {
    print "$i\n";
}
```





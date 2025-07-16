# Fetching data from hash

* keys
* sort keys

```perl
my @fields = keys %user;
foreach my $field (@fields) {
    print "$field    $user{$field}\n";
}


foreach my $field (keys %user) {
    print "$field    $user{$field}\n";
}


my @fields = keys %user;
my @sorted_fields = sort @fields;
foreach my $field (@sorted_fields) {
    print "$field    $user{$field}\n";
}

foreach my $field (sort keys %user) {
    print "$field    $user{$field}\n";
}
```



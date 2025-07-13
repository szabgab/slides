# Hashes

```
my %phone = (
    'Foo' => '01-23456',
    'Bar' => '98-76543',
);
say $phone{'Foo'};
$phone{'Zorg'} = '999'

for my $name (keys %phone) {
    say "$name $phone{$name}";
}
```



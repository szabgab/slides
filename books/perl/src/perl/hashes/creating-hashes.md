# Creating hashes

```perl
my %user;
%user = ("fname", "Foo", "lname", "Bar");

my %user = (
    "fname", "Foo", 
    "lname", "Bar",
    );

my %user = (
    fname => "Foo",
    lname => "Bar",
    );

print $user{"fname"}, "\n";
print $user{fname}, "\n";

my $key = "fname";
print $user{$key}, "\n";


$user{fname} = 'Moo';
$user{email} = 'foo@bar.com';
```



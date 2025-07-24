# Create hash from an array

```perl
my %user = qw(fname Foo lname Bar);

my @person = qw(fname Foo lname Bar);
my %user = @person;

my @foobar = %user;
print "@foobar\n"; # fname Foo lname Bar
                   # or
print "@foobar\n"; # lname Bar fname Foo 



$user{phone} = '123-456';     # change the value of one element
                              # or add key/value pair

%user = (phone => '123-456'); # change the hash
                              # remove all previous elements from the hash
                              # add a single key/value pair
```




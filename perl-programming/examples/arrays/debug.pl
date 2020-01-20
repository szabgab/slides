use strict;
use warnings;
use Data::Dumper qw(Dumper);

my @names_1 = ('Moose', 'Barney', 'Foo', 'Bar');
print "@names_1\n";         # Moose Barney Foo Bar


my @names_2 = ('Moose', 'Barney', 'Foo Bar');
print "@names_2\n";         # Moose Barney Foo Bar

print Dumper \@names_1;

print Dumper \@names_2;


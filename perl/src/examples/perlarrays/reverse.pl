use strict;
use warnings;

# LIST context
my @names = qw(Foo Bar Baz);
my @reverses_names = reverse @names;
print "@reverses_names\n";    #  Baz Bar Foo

# SCALAR context
my $string = "abcd";
my $reversed_string = reverse $string;
print "$reversed_string\n";   # dcba


use strict;
use warnings;
use Data::Dumper;

my %h = (
   a => 'Foo',
   b => localtime,
);

print Dumper \%h;
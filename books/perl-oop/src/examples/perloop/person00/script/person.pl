use strict;
use warnings;
use Data::Dumper qw(Dumper);

use Person;

my $figure = Person->new;

print $figure, "\n";

print Dumper $figure;

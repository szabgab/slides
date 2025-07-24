use strict;
use warnings;

use Text::CSV qw(csv);
use Data::Dumper qw(Dumper);

my $filename = 'planets.csv';
my $solar_system = csv(
    in => $filename,
    headers => 'auto');

print Dumper $solar_system;

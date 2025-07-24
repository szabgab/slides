use strict;
use warnings;

use Text::CSV qw(csv);
use Data::Dumper qw(Dumper);
use List::UtilsBy qw(sort_by);

my $filename = 'planets.csv';
my $solar_system = csv(
    in => $filename,
    headers => 'auto');

#print Dumper $solar_system;

#my @sorted = sort_by { $_->{'Planet name'} }  @$solar_system;
my @sorted = sort_by { $_->{'Mass'} }  @$solar_system;
print Dumper \@sorted;

my @sorted  = sort { $a->{'Planet name'} cmp $b->{'Planet name'} }
    @$solar_system;


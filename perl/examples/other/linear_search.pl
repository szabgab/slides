use strict;
use warnings;

my @planets = qw(Mercury Venus Earth Mars Jupiter Saturn);

sub search {
    my ($name, @items) = @_;

    for my $ix (0 .. $#items) {
        if ($items[$ix] eq $name) {
            return $ix;
        }
    }
    return;
}
print search('Mars', @planets), "\n";
print search('Pluto', @planets), "\n";


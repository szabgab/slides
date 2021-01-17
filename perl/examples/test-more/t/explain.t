use strict;
use warnings;

use Test::More tests => 1;

ok 1;

my $x = "String data";
my @y = ( 1, 2, 3 );
my %h = (
    foo => 'bar',
    numbers => [ 42, 17 ],
);

diag $x;
diag \@y;
diag \%h;

diag explain $x;
diag explain \@y;
note explain \%h;

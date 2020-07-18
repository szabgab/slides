use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 2;


is(sum(1, 1),    2,     '1+1');
is(sum(2, 2),    4,     '2+2');

my $x = "String data";
my $y = [ 1, 2, 3 ];
my %h = (
    foo => 'bar',
    numbers => [ 42, 17 ],
);

diag $x;
diag $y;
diag \%h;

diag explain $x;
diag explain $y;
diag explain \%h;

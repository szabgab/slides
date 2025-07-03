use strict;
use warnings;

use Test::More tests => 1;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');


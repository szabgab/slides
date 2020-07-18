use strict;
use warnings;
use v5.10;

use Test::More tests => 1;

use Person;

my $p = Person->new;
isa_ok($p, 'Person');


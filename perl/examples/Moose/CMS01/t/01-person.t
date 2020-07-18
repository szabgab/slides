use strict;
use warnings;

use Test::More;

plan tests => 2;

use_ok('CMS::Person');

my $p = CMS::Person->new;
isa_ok($p, 'CMS::Person');

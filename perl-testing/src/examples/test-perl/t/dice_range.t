use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 4;

use lib 't/lib';
use Test::Range qw(is_between);


for (1..4) {
    my $value = dice();
    is_between(1, '<=', $value, '<=', 6, 'in range');
}



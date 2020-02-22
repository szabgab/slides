use strict;
use warnings;

use Test::More tests => 1;

use lib 'lib';
use MyTools;


{
    my $result = fibonacci(-1);
    is($result, 0, 'fibonacci on -1 returns 0');
}



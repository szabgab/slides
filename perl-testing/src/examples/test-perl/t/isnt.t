use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More tests => 3;

foreach my $str ('Deep Purple', 'Beatles', 'ABBA') {
    isnt(scramble($str), $str,     $str);
}


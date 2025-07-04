use strict;
use warnings;

use Test::More tests => 2;
use Test::Warn;

use lib 'lib';
use MyTools;



{
    my $result;
    TODO: {
        local $TODO = 'fix warnings';
        warning_is {$result = sum()} undef, 'no warning in empty sum';
    }
    is($result, 0, 'result is ok');
}



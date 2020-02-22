use strict;
use warnings;

use lib 'lib';
use MyTools;

use Test::More;

{
    my $result = sum(1, 1);
    is $result, 2,  '1+1';
}

{
    my $result = sum(2, 2);
    is $result, 4,  '2+2';
}

done_testing;


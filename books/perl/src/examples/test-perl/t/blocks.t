use strict;
use warnings;

use MyTools;

use Test::More tests => 2;


{
    my $result = sum(1, 1);
    is $result, 2,  '1+1';
}

{
    my $result = sum(2, 2);
    is $result, 4,  '2+2';
}


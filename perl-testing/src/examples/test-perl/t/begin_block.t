use strict;
use warnings;

use MyTools;

use Test::More;
my $tests;

plan tests => $tests;


{
    my $result = sum(1, 1);
    is $result, 2,  '1+1';
    BEGIN { $tests += 1; }
}

{
    my $result = sum(2, 2);
    is $result, 4,  '2+2';
    BEGIN { $tests += 1; }
}


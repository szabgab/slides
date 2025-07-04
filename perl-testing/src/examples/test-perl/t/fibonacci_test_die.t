use strict;
use warnings;

use Test::More tests => 3;
use Test::Exception;

use lib 'lib';
use MyTools;


{
    my $result = fibonacci(3);
    is($result, 2, 'fibonacci on 3');
}
{
    dies_ok {fibonacci()} 'expecting to die';
}
{
    my $result = fibonacci(4);
    is($result, 3, 'fibonacci on 4');
}


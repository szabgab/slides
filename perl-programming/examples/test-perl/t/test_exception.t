use strict;
use warnings;

use Test::More tests => 2;
use Test::Exception;

is div(6, 2), 3, 'div by 2';
throws_ok { div(8, 0) } qr/division by zero/, 'div by zero';


sub div {
    my ($x, $y) = @_;
    return $x/$y;
}

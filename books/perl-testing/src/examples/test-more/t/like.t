use strict;
use warnings;

use Test::More tests => 2;

like( foo(), qr/\d+/, "there are some digits in the result" );
like( bar(), qr/\d+/, "there are some digits in the result" );

sub foo {
    return "This is a long text with a number 42 in it";
}
sub bar {
    return "This is another string with no number in it";
}

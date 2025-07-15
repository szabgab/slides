package MyAttributes;
use strict;
use warnings;

use Attribute::Handlers;
 
sub UNIVERSAL::Foo : ATTR(SCALAR) {
    print "Foo\n";
}

sub UNIVERSAL::Bar : ATTR(SCALAR) {
    print "Bar\n";
}

1;


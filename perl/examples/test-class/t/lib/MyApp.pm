package t::lib::MyApp;
use strict;
use warnings;

use base 'Test::Class';
use Test::More;

use MyApp qw(add);

sub test_add : Test {
    is add(2, 3), 5;
}

1;

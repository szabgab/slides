package Test::MyApp;
use strict;
use warnings;

use base 'Test::Class';
use Test::More;

use MyApp qw(add div);

sub test_add : Test {
    is add(2, 3), 5;
}

sub test_div : Test {
    is div(8, 2), 4;
}


Test::Class->runtests;

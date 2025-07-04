#!perl

use strict;
use warnings;

use Test::More;
use Test::BDD::Cucumber::StepFile;

use lib 'examples/basic/lib/';
use HelloWorld;

Given 'the HelloWorld module', sub {
};

When qr/^calling hello_world function/, sub {
    S->{'result'}  = HelloWorld::hello_world();
};

Then qr/return is "(.+)"/, sub {
    my $expected = C->matches->[0];
    is S->{'result'}, $expected;
};


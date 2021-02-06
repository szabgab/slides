#!perl

use strict;
use warnings;

use Test::More;
use Test::BDD::Cucumber::StepFile;

use File::Basename qw(dirname);
use File::Spec;
use lib File::Spec->catfile(dirname(__FILE__), '..', '..', 'lib');
use Calculator;

Given 'the calculator app', sub {
    S->{'calculator'} = 'Calculator';
};
#
#When qr/^calling hello_world function/, sub {
#    S->{'result'}  = HelloWorld::hello_world();
#};
#
Then qr/display is "([^"]*)"/, sub {
    my $expected = C->matches->[0];
    my $function = S->{'calculator'} . '::display';
    no strict 'refs';
    is $function->(), $expected;
};


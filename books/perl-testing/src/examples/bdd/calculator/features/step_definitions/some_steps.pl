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
    Calculator::reset();
};

When qr/^clicked on (.)/, sub {
    Calculator::click(C->matches->[0]);
};

Then qr/display is "([^"]*)"/, sub {
    my $expected = C->matches->[0];
    is Calculator::display(), $expected;
};

Then qr/the history is/, sub {
    my $expected = C->data;
    is Calculator::history(), $expected;
};


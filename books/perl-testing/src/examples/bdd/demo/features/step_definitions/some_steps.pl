#!perl

use strict;
use warnings;

use Test2::Bundle::More;
use Test::BDD::Cucumber::StepFile;


Given qr/a Fixture called (\S+)/, sub {
    my $name = $1;
    diag "The fixture is $name";
    ok 1, "OK $name";   # really $1 as in the tutorial?
};

Given qr/a (\S+) object/, sub {
    my $name = C->matches->[0];
    ok 1, "OK $name";
};

When qr/I've added "(.+)" to the object/, sub {
    push @{ S->{'object'} }, C->matches->[0];
};


Before sub {
    diag 'before';
};

After sub {
    my $c = shift;

    diag 'after'
    # $c->stash->{'scenario'}->{'Calculator'};
};

Then qr/^the output is "(.+)"/, sub {
    my ($value) = @{ C->matches };
    ok 1, "expected output is $value";
};

Then qr/^the error is "(.*)"/, sub {
    my ($value) = @{ C->matches };
    ok 1, "expected error is $value";
    #is "expected", "recived", "demo";
};


# Transform qr/^(__THE_NUMBER_\w+__)$/, sub { map_word_to_number($1) };
# Transform qr/^table:number as word$/, sub {

# S->{'object'}->add( C->data );
#



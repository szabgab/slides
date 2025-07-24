#!/usr/bin/perl
use strict;
use warnings;

use English qw( -no_match_vars ) ;
use Carp qw(croak carp);
use Exception::Class (
    'Number::Small' => {
        fields => [ 'number' ],
    },
    'Number::Big' => {
        fields => [ 'number' ],
    },
    'Number::Missing' => {},
    'Number::Invalid' => {
        fields => [ 'input' ],
    },
);

sub Number::Invalid::full_message {
    my ($self) = @_;
    return
        sprintf("We received '%s' while the input must be a number.",
        $self->input);
}

sub Number::Small::full_message {
    my ($self) = @_;
    return "number " . $self->number . " is too small";
}

sub Number::Big::full_message {
    my ($self) = @_;
    return "number " . $self->number . " is too big";
}
sub Number::Missing::full_message {
    my ($self) = @_;
    return "number is missing";
}



# Throwing exceptions
sub check_number {
    my ($num) = @_;
    if (not defined $num) {
        Number::Missing->throw();
    }
    if ($num !~ /^\d+$/) {
        Number::Invalid->throw(input => $num);
    }

    if ($num < 0) {
        Number::Small->throw(number => $num);
    }
    if ($num > 100) {
        Number::Big->throw(number => $num);
    }
}


# Catching exceptions
eval {
    check_number(@ARGV);
};
if ($EVAL_ERROR) {
    if (Number::Missing->caught) {
        print "$EVAL_ERROR\n";
        print "Usage: $0 NUMBER\n";
        exit;
    }
    if (Number::Small->caught() or Number::Big->caught) {
        print "$EVAL_ERROR\n";
        print "Number must be between 0-100\n";
        exit;
    }

    # error that I don't know how to handle:
    croak $EVAL_ERROR;
}
print "Number was ok\n";



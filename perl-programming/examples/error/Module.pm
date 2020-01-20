package Module;
use strict;
use warnings;

use Carp qw(carp cluck);

sub f {
    my ($x) = @_;
 
    warn "Parameter needs to be a number" if $x =~ /\D/;
    return $x;
}

sub g {
    my ($x) = @_;
 
    carp "Parameter needs to be a number" if $x =~ /\D/;
    return $x;
}

sub h {
    my ($x) = @_;
 
    cluck "Parameter needs to be a number" if $x =~ /\D/;
    return $x;
}


1;

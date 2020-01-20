package App::Code;
use strict;
use warnings;

use Carp::Clan qw(^App::);
use Carp ();

sub f {
    my ($x) = @_;
 
    warn "Parameter needs to be a number" if $x =~ /\D/;
    return $x;
}

sub g {
    my ($x) = @_;
 
    Carp::carp "Parameter needs to be a number" if $x =~ /\D/;
    return $x;
}

sub h {
    my ($x) = @_;
 
    carp "Parameter needs to be a number" if $x =~ /\D/;
    return $x;
}


1;

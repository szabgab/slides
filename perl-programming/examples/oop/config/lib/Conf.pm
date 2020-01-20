package Conf;
use strict;
use warnings;

my $instance;

sub new {
    my ($class) = @_;
    
    die "Called ->new again" if $instance;

    $instance = {};

    bless $instance, $class;

    # Read the configuration ....

    return $instance;
}

sub instance {
    my ($self) = @_;
    
    die "Called ->instance before calling ->new" if not $instance;

    return $instance;
}


1;

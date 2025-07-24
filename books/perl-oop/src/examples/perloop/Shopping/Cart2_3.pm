package Shopping::Cart2_3;
use strict;
use warnings;

use Data::Dumper;

sub new {
    my ($class) = @_;

    my $self = {};

    bless $self, $class;

    return $self;
}

sub set_name {
    my ($self, $person_name) = @_;
    $self->{name} = $person_name;
}

sub get_name {
    my ($self) = @_;
    return $self->{name};
}

1;


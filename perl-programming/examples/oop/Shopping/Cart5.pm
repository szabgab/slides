package Shopping::Cart5;
use strict;
use warnings;

use Data::Dumper;

sub new {
    my ($class, $name) = @_;

    my $self = bless {}, $class;

    $self->name($name);

    return $self;
}

sub name {
    my ($self, $name) = @_;
    if (defined $name) {
        $self->{name} = $name;
    }

    return $self->{name};
}

sub add {
    my ($self, $name) = @_;

    $self->{CART}{$name}++;

    return 1;
}

1;


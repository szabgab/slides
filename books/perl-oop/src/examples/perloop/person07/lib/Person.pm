package Person;
use strict;
use warnings;

sub new {
    my ($class, %args) = @_;

    my $self = \%args;

    bless $self, $class;

    return $self;
}

sub lname {
    my ($self, $value) = @_;

    return $self->{lname};
}

sub marry {
    my ($self, $other) = @_;

    return $self->{lname} =     $self->{lname} . '-' . $other->lname;
}


1;

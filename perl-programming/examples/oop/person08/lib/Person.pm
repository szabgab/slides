package Person;
use strict;
use warnings;

sub new {
    my ($class, %args) = @_;

    my $self = \%args;

    bless $self, $class;

    return $self;
}

sub fname {
    my ($self, $value) = @_;

    return $self->{fname};
}

sub lname {
    my ($self, $value) = @_;

    return $self->{lname};
}


1;

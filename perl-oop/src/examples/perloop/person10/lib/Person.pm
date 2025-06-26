package Person;
use strict;
use warnings;

sub new {
    my ($class, %args) = @_;

    my $self = \%args;

    bless $self, $class;

    return $self;
}

sub name {
    my ($self, $value) = @_;

    return $self->{name};
}

DESTROY {
    my ($self) = @_;
    print $self->name, " is dying\n";
}

1;

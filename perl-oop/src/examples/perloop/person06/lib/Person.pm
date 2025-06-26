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
    if (@_ == 2) {
        $self->{lname} = $value;
    }

    return $self->{lname};
}

sub fname {
    my ($self) = @_;

    return $self->{fname};
}


1;

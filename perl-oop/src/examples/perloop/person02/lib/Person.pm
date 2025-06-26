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
    if (@_ == 2) {
        $self->{name} = $value;
    }

    return $self->{name};
}

sub year {
    my ($self, $value) = @_;
    if (@_ == 2) {
        die qq{Attribute (year) does not pass the type constraint because: } .
            qq{Validation failed for 'Int' with value "$value"}
            if $value !~ /^\d+$/;
        $self->{year} = $value;
    }

    return $self->{year};
}

1;


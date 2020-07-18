package Person;
use strict;
use warnings;

my $count = 0;

sub new {
    my ($class, %args) = @_;

    my $self = \%args;

    bless $self, $class;

    $count++;

    return $self;
}


sub name {
    my ($self, $value) = @_;

    return $self->{name};
}


sub count {
    return $count;
}

1;

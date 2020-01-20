package Person;
use strict;
use warnings;

sub new {
    my ($class) = @_;

    my $self = {};

    bless $self, $class;

    return $self;
}


1;


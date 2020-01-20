package Employee;
use strict;
use warnings;

use parent 'Person';

sub new {
    my ($class, %args) = @_;

    my $employer = delete $args{employer};

    my $self = $class->SUPER::new(%args);

    $self->{employer} = $employer;

    return $self;
}

sub employer {
    my ($self, $value) = @_;
    if (@_ == 2) {
        $self->{employer} = $value;
    }

    return $self->{employer};
}

1;


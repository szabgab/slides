package Employee;
use strict;
use warnings;

use parent 'Person';

sub employer {
    my ($self, $value) = @_;
    if (@_ == 2) {
        $self->{employer} = $value;
    }

    return $self->{employer};
}

1;


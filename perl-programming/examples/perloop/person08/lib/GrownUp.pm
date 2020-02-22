package GrownUp;
use strict;
use warnings;

use parent 'Person';

use overload
    '""' => \&stringify;

sub stringify {
    my ($self) = @_;
    return $self->fname . ' ' . $self->lname;
}


1;

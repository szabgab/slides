package Line3D;
use strict;
use warnings;

use base 'Line';

sub length {
    my ($self) = @_;

    my $x = $self->p1->get_x - $self->p2->get_x;
    my $y = $self->p1->get_y - $self->p2->get_y;
    my $z = $self->p1->get_z - $self->p2->get_z;

    return sqrt($x**2 + $y**2 + $z**2);
}


1;

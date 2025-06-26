package Point;
use strict;
use warnings;

our $VERSION = '0.01';

=head1 NAME

Point - example of a Point

=cut

sub new {
    my ($class, %args) = @_;

#    my $self = {};
#    bless $self, $class;

    my $self = bless {}, $class;

    $self->set_x($args{x});
    $self->set_y($args{y});

    return $self;
}

sub get_x {
    my ($self) = @_;

    return $self->{x};
}

sub set_x {
    my ($self, $value) = @_;

    $self->{x} = $value;

    return;
}


sub get_y {
    my ($self) = @_;

    return $self->{y};
}



sub set_y {
    my ($self, $value) = @_;

    $self->{y} = $value;

    return;
}


1;

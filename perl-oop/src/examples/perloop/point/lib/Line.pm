package Line;
use strict;
use warnings;

sub new {
    my ($class, @args) = @_;
    my $self = bless {}, $class;

    $self->p1(shift @args);
    $self->p2(shift @args);

    return $self;
}

sub p1 {
    my ($self, $value) = @_;
    if ($value) {
        $self->{p1} = $value;
    }
    return $self->{p1};
}

sub p2 {
    my ($self, $value) = @_;
    if ($value) {
        $self->{p2} = $value;
    }
    return $self->{p2};
}

sub length {
    my ($self) = @_;

    my $x = $self->p1->get_x - $self->p2->get_x;
    my $y = $self->p1->get_y - $self->p2->get_y;

    return sqrt($x**2 + $y**2);
}


1;

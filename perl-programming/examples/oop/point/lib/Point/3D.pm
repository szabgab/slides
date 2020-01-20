package Point::3D;
use strict;
use warnings;

use base 'Point';

sub new {
	my ($class, %args) = @_;

	my $z = delete $args{z};

	my $self = $class->SUPER::new(%args);

	$self->set_z($z);

	return $self;
}

sub get_z {
	my ($self) = @_;

	return $self->{z};
}

sub set_z {
	my ($self, $value) = @_;

	$self->{z} = $value;

	return;
}

1;

package Point::Small;
use strict;
use warnings;


use base 'Point';

use Carp qw(croak);

sub set_x {
	my ($self, $value) = @_;

	if (0 <= $value and $value < 100) {
		$self->SUPER::set_x($value);
		return;
	}

	#die "Coordinate x needs to be between 0 and 100. Currently it is '$value'";
	croak "Coordinate x needs to be between 0 and 100. Currently it is '$value'";
}

sub set_y {
	my ($self, $value) = @_;

	if (0 <= $value and $value < 100) {
		$self->SUPER::set_y($value);
		return;
	}

	croak "Coordinate y needs to be between 0 and 100. Currently it is '$value'";
}

AUTOLOAD {
	#Carp::cluck("A");
	our $AUTOLOAD;
	print "AUTO: $AUTOLOAD\n";
}

DESTROY {
}

1;

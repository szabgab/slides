package Games::Spacefight;
use Moose;
use MooseX::Singleton;
use v5.10;

use Games::Spacefight::Ship;

has range => (is => 'rw');

sub run {
	my ($self, @args) = @_;
	say $self;
	say @args;
	
	$self->range()
	
	
#	while (1) {
#		my $enemy = Games::Spacefight::Ship->new;
#		last;
#	}
}

1;


package Person;
use Moose;


has 'name' => (is => 'rw');
has 'year' => (isa => 'Int', is => 'rw');

has 'birthday' => (isa => 'DateTime', is => 'rw');


sub age {
	my $self = shift;
	my $bd = $self->birthday or die 'No birthday';

	require DateTime;
	return DateTime->now - $bd;
}


1;


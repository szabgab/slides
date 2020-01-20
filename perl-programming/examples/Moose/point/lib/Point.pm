package Point;
use Moose;

has 'x' => (isa => 'Int', is => 'rw');
has 'y' => (isa => 'Int', is => 'rw');

has 'name' => (isa => 'Str', is => 'ro');


sub set_name {
    my ($self, $value) = @_;
    $self->{name} = $value;
}

sub clear {
    my $self = shift;
    $self->x(0);
    $self->y(0);    
}



1;

# based on Moose::Cookbook::Recipe1


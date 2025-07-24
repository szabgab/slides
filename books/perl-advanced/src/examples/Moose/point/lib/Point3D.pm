package Point3D;
use Moose;

extends 'Point';

has 'z' => (is => 'rw', isa => 'Int');

after 'clear' => sub {
    my $self = shift;
    $self->{z} = 0;
};

1;

# taken from Moose::Cookbook::Recipe1

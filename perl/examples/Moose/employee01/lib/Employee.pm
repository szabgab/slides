package Employee;
use Moose;

extends 'Person';

has 'employer'   => (is => 'rw');

1;


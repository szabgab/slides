package Simple::Strict;
use Moose;
use MooseX::StrictConstructor;

has 'fname' => (is => 'rw', isa => 'Str');

1;


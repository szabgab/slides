package CMS::Person;
use 5.010001;
use Moose;

our $VERSION = '0.01';

has 'fname' => (
    is => 'ro', 
    isa => 'Str'
);

1;

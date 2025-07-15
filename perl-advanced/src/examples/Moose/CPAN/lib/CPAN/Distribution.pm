package CPAN::Distribution;
use Moose;

has version => (is => 'ro', isa => 'Str');
has name    => (is => 'ro', isa => 'Str');

has files   => (is => 'ro', isa => 'ArrayRef[Str]');


1;


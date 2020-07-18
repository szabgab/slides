package Games::Spacefight::Ship;
use Moose;
use v5.10;

my $SIZE = 200;

has location => (
	isa => 'Int',
	is  => 'ro',
	default => int rand $SIZE,
);



1;

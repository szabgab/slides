package BinaryTree;
use 5.010;
use Moose;

use Carp ();

has 'node' => (is => 'rw', isa => 'Any');

has 'parent' => (
	is  => 'rw',
	isa => 'BinaryTree',
	predicate => 'has_parent',
	week_ref => 1,
);

has 'left' => (
	is  => 'rw',
	isa => 'BinaryTree',
	predicate => 'has_left',
	#lazy => 1,
	#default => sub { BinaryTree->new( parent => shift, @_) },
	trigger => \&_set_parent_for_child,
);

sub add_left {
	my $self = shift;
	Carp::confess("node already has left") if $self->has_left;
	return $self->left( BinaryTree->new(@_) );
}

sub _set_parent_for_child {
	my ($self, $child) = @_;
#	die "@_";
	Carp::confess "You cannot insert a tree which already has a parent"
		if $child->has_parent;
	$child->parent($self);
}

1;


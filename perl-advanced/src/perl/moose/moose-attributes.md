# Moose Attributes Overview

```perl
# accessors, mutators, getters, setters
has 'x' => (is => 'rw');
has 'x' => (is => 'ro');
has 'x' => (is => 'bare');

# types
has 'x' => (is => 'rw', isa => 'Int');
has 'y' => (is => 'rw', isa => 'Str');

# required
has 'z' => (
    is => 'ro',
    isa => 'Str',
    required => 1,
);

# default
has 'x' => (
    is => 'rw',
    isa => 'Int',
    default => 42,
);
has 'names' => (
    is => 'rw',
    isa => 'HashRef',
    default => sub { {} },
);

has 'names' => (
    is => 'rw',
    isa => 'HashRef',
    builder => '_build_name',
);
sub _build_name {
    my $self = shift;
	# ...
	return {};
}
```



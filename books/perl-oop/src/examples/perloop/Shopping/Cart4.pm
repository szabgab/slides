package Shopping::Cart4;
use strict;
use warnings;

use Data::Dumper;

sub new {
    my ($class, $name) = @_;

    my $self = bless {}, $class;

    $self->name($name);

    return $self;
}

sub name {
    my ($self, $name) = @_;
    if (defined $name) {
        $self->{name} = $name;
    }

    return $self->{name};
}


1;


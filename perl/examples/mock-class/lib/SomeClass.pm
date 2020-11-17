package SomeClass;
use strict;
use warnings;

sub new {
    my ($class) = @_;
    print "new\n";
    my $self = bless {}, $class;

    return $self;
}

sub name {
    my ($self, $value) = @_;
    print "name\n";
    if (@_ == 2) {
        $self->{name} = $value;
    }
    return $self->{name};
}

sub double {
    my ($self, $value) = @_;
    print "double\n";

    return 2 * $value;
}

1;


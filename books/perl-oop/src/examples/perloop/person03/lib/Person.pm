package Person;
use strict;
use warnings;

use Scalar::Util qw(blessed);

sub new {
    my ($class, %args) = @_;

    my $self = \%args;

    bless $self, $class;

    return $self;
}

sub name {
    my ($self, $value) = @_;
    if (@_ == 2) {
        $self->{name} = $value;
    }

    return $self->{name};
}

sub birthday {
    my ($self, $value) = @_;
    if (@_ == 2) {
       die qq{Attribute (birthday) does not pass the type constraint because:} .
           qq{Validation failed for 'DateTime' with value 1988 at accessor}
            if not blessed $value or not $value->isa('DateTime') ;
        $self->{birthday} = $value;
    }

    return $self->{birthday};
}

1;


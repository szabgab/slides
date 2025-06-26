package Person;
use strict;
use warnings;

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

sub sex {
    my ($self, $value) = @_;
    if (@_ == 2) {
        $value = lc substr($value, 0, 1);
        die qq{Attribute (sex) does not pass the type constraint because:}
            if $value ne 'm' and $value ne 'f' ;
        $self->{sex} = $value;
    }

    return $self->{sex};
}

1;


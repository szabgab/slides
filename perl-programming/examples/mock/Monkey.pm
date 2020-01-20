package Monkey;
use strict;
use warnings;

sub new {
    my ($class, $count) = @_;
    return bless { bananas => $count }, $class;
}

sub is_hungry {
    my ($self) = @_;

    my $hungry = 1;  # ... check if I am hungray.
    if ($hungry) {
        $self->eat();
    }
    return $hungry;     
}

sub eat {
    my ($self) = @_;

    $self->{bananas}--;
}

sub bananas {
    my ($self)  = @_;
    return $self->{bananas};
}

1;


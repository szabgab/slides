package MyClass;
use v5.10;
use strict;
use warnings;

sub new {
    my ($class, %params) = @_;
    my $self = bless {}, $class;
    for my $field (keys %params) {
        $self->{$field} = $params{$field};
    }
}

sub some_action {
    my ($slef, @params) = @_;

    # $self->{field} 

    my $result = 42;

    return $result;
} 

1;


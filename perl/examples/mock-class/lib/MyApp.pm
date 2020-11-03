package MyApp;
use strict;
use warnings;

use MyClass;

sub give_name {
    my ($name) = @_;

    my $obj = MyClass->new;
    $obj->name($name);

    return $obj->name;
}

sub double {
    my ($n) = @_;

    my $obj = MyClass->new;
    return $obj->double($n);
}

1;



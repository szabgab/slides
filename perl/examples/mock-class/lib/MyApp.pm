package MyApp;
use strict;
use warnings;

use SomeClass;

sub give_name {
    my ($name) = @_;

    my $obj = SomeClass->new;
    $obj->name($name);

    return $obj->name;
}

sub double {
    my ($n) = @_;

    my $obj = SomeClass->new;
    return $obj->double($n);
}

1;



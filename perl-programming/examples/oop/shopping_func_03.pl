#!/usr/bin/perl
use strict;
use warnings;

my @users;
push @users, new_cart();
set_name($users[0], 'Foo');

printf "The name is '%s'\n", get_name($users[0]);

sub new_cart {
    return {};
}

sub set_name {
    my ($cart, $person_name) = @_;
    $cart->{name} = $person_name;
}
sub get_name {
    my ($cart) = @_;
    return $cart->{name};
}


#!/usr/bin/perl
use strict;
use warnings;

my @users;
push @users, new_cart();
set_name($users[0], 'Foo');

printf "The name is '%s'\n", get_name($users[0]);
add_item($users[0], 'The OOP book of Damian');
my %books = list_cart($users[0]);
_print(%books);

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

sub add_item {
    my ($cart, $product, $amount) = @_;
    $amount ||= 1;
    $cart->{CART}{$product} += $amount;
}

sub list_cart {
    my ($cart) = @_;
    return %{ $cart->{CART} };
}

sub _print {
    my %books = @_;
    foreach my $title (sort keys %books) {
        print "$title    $books{$title}\n";
    }
}



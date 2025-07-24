package Shopping::Cart::Functions;
use strict;
use warnings;

use base 'Exporter';
our @EXPORT = qw(get_price new_cart set_name get_name add_item list_cart);

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
    my ($cart, $product_name, $amount) = @_;
    $amount ||= 1;
    $cart->{CART}{$product_name} += $amount;
}

sub remove_item {
    my ($cart, $product_name, $amount) = @_;
    $amount ||= 1;
    $cart->{CART}{$product_name} -= $amount;
}

sub list_cart {
    my ($cart) = @_;
    return %{ $cart->{CART} };
}

sub get_price {
    my ($cart) = @_;

    my %prices = (
        'The OOP book of Damian'          => 23,
        'Perl Best Practices of Damian'   => 17,
        'The Little Prince'               => 8,
        'Objectives and Classifications'  => 48,
        'Winnie The Pooh'                 => 11,
    );

    my $price = 0;
    foreach my $entry (keys %{ $cart->{CART} }) {
         $price += $cart->{CART}{$entry} * $prices{$entry};
    }
    return $price;
}


1;


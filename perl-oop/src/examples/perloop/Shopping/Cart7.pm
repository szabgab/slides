package Shopping::Cart::OOP;
use strict;
use warnings;

my %prices = (
    'The OOP book of Damian'          => 23,
    'Perl Best Practices of Damian'   => 17,
    'The Little Prince'               => 8,
    'Objectives and Classifications'  => 48,
    'Winnie The Pooh'                 => 11,
);


sub new {
    my ($class) = @_;

    my $self = {};

    bless $self, $class;

    return $self;
}

sub set_name {
    my ($self, $person_name) = @_;
    $self->{name} = $person_name;
}

sub get_name {
    my ($self) = @_;
    return $self->{name};
}


sub add_item {
    my ($self, $product_name, $amount) = @_;
    $amount ||= 1;
    $self->{CART}{$product_name} += $amount;
}

sub remove_item {
    my ($self, $product, $amount) = @_;
    $amount ||= 1;
    $self->{CART}{$product} -= $amount;
}

sub list_cart {
    my ($self) = @_;
    return %{ $self->{CART} };
}

sub get_price {
    my ($self) = @_;

    my $price = 0;
    foreach my $entry (keys %{ $self->{CART} }) {
         $price += $self->{CART}{$entry} * $prices{$entry};
    }

    return $price;
}

1;


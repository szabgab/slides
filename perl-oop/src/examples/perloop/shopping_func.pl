#!/usr/bin/perl
use strict;
use warnings;

my @users;
push @users, {};
$users[0]{name} = 'Foo';
$users[0]{CART}{'The OOP book of Damian'}++;
$users[0]{CART}{'Perl Best Practices of Damian'}++;
printf "Current price for %s is %s\n", $users[0]{name}, get_price($users[0]);

push @users, {};
$users[1]{name} = 'Bar';
$users[1]{CART}{'The Little Prince'}++;

$users[0]{CART}{'The OOP book of Damian'}++;
$users[0]{CART}{'Objectives and Classifications'}++;

printf "Current price for %s is %s\n", $users[0]{name}, get_price($users[0]);

my %books1 = %{ $users[0]{CART} };
_print(%books1);

$users[1]{CART}{'Winnie The Pooh'} += 3;

$users[0]{CART}{'Perl Best Practices of Damian'}++;
printf "Current price for %s is %s\n", $users[0]{name}, get_price($users[0]);
printf "Current price for %s is %s\n", $users[1]{name}, get_price($users[1]);
my %books2 = %{ $users[0]{CART} };
_print(%books2);


sub _print {
    my %books = @_;
    foreach my $title (sort keys %books) {
        print "$title    $books{$title}\n";
    }
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


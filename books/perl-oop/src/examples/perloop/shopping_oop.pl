#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart::OOP;

my @users;
push @users, Shopping::Cart::OOP->new_cart;
$users[0]->set_name('Foo');
$users[0]->add_item('The OOP book of Damian');
$users[0]->add_item('Perl Best Practices of Damian');
printf "Current price is %s\n", $users[0]->get_price();

push @users, Shopping::Cart::OOP->new_cart;
$users[1]->set_name('Bar');
$users[1]->add_item('The Little Prince');

$users[0]->add_item('The OOP book of Damian');
$users[0]->add_item('Objectives and Classifications');

printf "Current price for %s is %s\n", $users[0]->get_name, $users[0]->get_price();

my %books1 = $users[0]->list_cart();
_print(%books1);

$users[1]->add_item('Winnie The Pooh', 3);

$users[0]->add_item('Perl Best Practices of Damian');
printf "Current price for %s is %s\n", $users[0]->get_name, $users[0]->get_price();
printf "Current price for %s is %s\n", $users[1]->get_name, $users[1]->get_price();
my %books2 = $users[0]->list_cart();
_print(%books2);


sub _print {
    my %books = @_;
    foreach my $title (sort keys %books) {
        print "$title    $books{$title}\n";
    }
}


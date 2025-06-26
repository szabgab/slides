#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart;

my @users;
push @users, Shopping::Cart->new_cart;
$users[0]->set_name('Foo');
$users[0]->add('The OOP book of Damian');
$users[0]->add('Perl Best Practices of Damian');
printf "Current price is %s\n", $users[0]->get_price();

push @users, Shopping::Cart->new_cart;
$users[1]->set_name('Bar');
$users[1]->add('apple');

$users[1]->add('The OOP book of Damian');
$users[1]->add('Objectives and Classifications');

printf "Current price is %s\n", $users[0]->get_price();

my %books = $users[0]->get_list();
_print(%books);

$users[1]->add('banana', 3);

$users[0]->remove('Perl Best Practices of Damian');
printf "Current price is %s\n", $users[0]->get_price();
%books = $users[0]->get_list();
_print(%books);



sub _print {
    my %books = @_;
    foreach my $title (sort keys %books) {
        print "$title    $books{$title}\n";
    }
}


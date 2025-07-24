#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';
use Shopping::Cart::Functions;

my @users;
push @users, new_cart();
set_name($users[0], 'Foo');
add_item($users[0], 'The OOP book of Damian');
add_item($users[0], 'Perl Best Practices of Damian');
printf "Current price for %s is %s\n", get_name($users[0]), get_price($users[0]);

push @users, new_cart();
set_name($users[1], 'Bar');
add_item($users[1], 'The Little Prince');

add_item($users[0], 'The OOP book of Damian');
add_item($users[0], 'Objectives and Classifications');

printf "Current price for %s is %s\n", get_name($users[0]), get_price($users[0]);

my %books1 = list_cart($users[0]);
_print(%books1);

add_item($users[1], 'Winnie The Pooh', 3);

add_item($users[0], 'Perl Best Practices of Damian');
printf "Current price for %s is %s\n", get_name($users[0]), get_price($users[0]);
printf "Current price for %s is %s\n", get_name($users[1]), get_price($users[1]);
my %books2 = list_cart($users[0]);
_print(%books2);


sub _print {
    my %books = @_;
    foreach my $title (sort keys %books) {
        print "$title    $books{$title}\n";
    }
}



#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';
use Shopping::Cart::Listed;

my $cart_of_foo = Shopping::Cart::Listed->new(name => 'Foo');
{
    my $cart_of_bar = Shopping::Cart::Listed->new(name => 'Bar');
    _print_names();
}

my $cart_of_moo = Shopping::Cart::Listed->new(name => 'Moo');
_print_names();

print "END of script\n";

sub _print_names {
    foreach my $name (Shopping::Cart::Listed->list_names) {
        print "$name\n";
    }
}

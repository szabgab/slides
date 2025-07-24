#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart::Exercise;

my $foo = Shopping::Cart::Exercise->new('Foo');
$foo->add_item('The Little Prince');
printf "Current price for %s is %s\n", $foo->get_name, $foo->get_price();

$foo->set_name();
$foo->set_name("abc2");

my $bar = Shopping::Cart::Exercise->new('Bar2');
$bar->set_name('Bar');

print $bar->get_name('Moo'), "\n";

print Shopping::Cart::Exercise->get_object_count(), "\n";
eval {
    print $foo->get_object_count, "\n";
    print "This should not be printed\n";
};
print $@;

{
    my $moo = Shopping::Cart::Exercise->new('Moo');
    print "In the block\n";
    print Shopping::Cart::Exercise->get_object_count(), "\n";
    print Shopping::Cart::Exercise->get_existing_object_count(), "\n";
}
print "After block\n";
print Shopping::Cart::Exercise->get_object_count(), "\n";
print Shopping::Cart::Exercise->get_existing_object_count(), "\n";




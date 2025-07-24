#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::Cart::Bonus;

my $foo = Shopping::Cart::Bonus->new('Foo');
$foo->add_item('The Little Prince');

my $bar = Shopping::Cart::Bonus->new();
$bar->set_name('Bar');

{
    my $moo = Shopping::Cart::Bonus->new('Moo');
    print Shopping::Cart::Bonus->get_object_count(), "\n";
    print Shopping::Cart::Bonus->get_existing_object_count(), "\n";
}
print "-----------\n";
print Shopping::Cart::Bonus->get_object_count(), "\n";
print Shopping::Cart::Bonus->get_existing_object_count(), "\n";
foreach my $o (Shopping::Cart::Bonus->list_objects()) {
    print $o->get_name, "\n";
}


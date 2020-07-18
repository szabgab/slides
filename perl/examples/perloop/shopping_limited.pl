#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/oop';

use Shopping::LimitedCart;

my @carts;
foreach (1..4) {
    push @carts, Shopping::LimitedCart->new;
}
printf("After 4th: %s %s\n",
    Shopping::LimitedCart->get_object_count(),
    Shopping::LimitedCart->get_existing_object_count());
{
    my $foo = Shopping::LimitedCart->new;
    printf("After the 5th: %s %s\n",
        Shopping::LimitedCart->get_object_count(),
        Shopping::LimitedCart->get_existing_object_count());
    my $bar = Shopping::LimitedCart->new;
    printf("After the 6th: %s %s\n",
        Shopping::LimitedCart->get_object_count(),
        Shopping::LimitedCart->get_existing_object_count());
}

printf("After getting out of the block: %s %s\n",
    Shopping::LimitedCart->get_object_count(),
    Shopping::LimitedCart->get_existing_object_count());
my $moo = Shopping::LimitedCart->new;
printf("After the 7th: %s %s\n",
    Shopping::LimitedCart->get_object_count(),
    Shopping::LimitedCart->get_existing_object_count());


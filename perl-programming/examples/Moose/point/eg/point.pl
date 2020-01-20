#!/usr/bin/perl 
use strict;
use warnings;

use lib 'lib';

use Point;

my $p = Point->new;

$p->x(10);
$p->y(20);

printf "Coordinates: x: %s, y %s\n", $p->x, $p->y;

# $p->name("Foo");
# would throw an exception

$p->set_name("Bar");
print $p->name, "\n";

my $p2 = Point->new(name => 'Foo');
print $p->name, "\n";



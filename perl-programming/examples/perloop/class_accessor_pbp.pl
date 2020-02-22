#!/usr/bin/perl
use strict;
use warnings;


package Car;
use strict;
use warnings;

use base 'Class::Accessor';
__PACKAGE__->follow_best_practice;
__PACKAGE__->mk_accessors(qw(type color cc weight));

package main;

my $peugeot = Car->new;
$peugeot->set_cc(1500);
$peugeot->set_color('green');


print $peugeot->get_color(), "\n";


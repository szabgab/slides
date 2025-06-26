#!/usr/bin/perl
use strict;
use warnings;


package Car;
use strict;
use warnings;

use base 'Class::Accessor';
__PACKAGE__->mk_accessors(qw(type color cc weight));

package main;

my $peugeot = Car->new;
$peugeot->cc(1500);
$peugeot->color('green');


print $peugeot->color(), "\n";


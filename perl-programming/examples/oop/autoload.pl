#!/usr/bin/perl 
use strict;
use warnings;



package Car;
use strict;
use warnings;

use Data::Dumper;

sub new {
    bless {}, shift;
}


our $AUTOLOAD;

AUTOLOAD {
    print "Calling $AUTOLOAD with parameters " . Dumper \@_;

}


package main;


my $car = Car->new("Porsche");
$car->drive("fast");


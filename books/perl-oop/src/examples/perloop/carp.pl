#!/usr/bin/perl 
use strict;
use warnings;




package Car;
use strict;
use warnings;
use Carp qw(carp);


sub first {
    carp "first";
    second();
}

sub second {
    carp "second";
    third();
}

sub third {
    carp "third";
    Moped::fourth();
}

package Moped;
use strict;
use warnings;
use Carp qw(carp);

sub fourth {
    carp "fourth";
}




package main;

Car::first();




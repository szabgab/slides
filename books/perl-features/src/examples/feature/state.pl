#!/usr/bin/perl 
use strict;
use warnings;

use 5.010;

sub next_counter {
    state $counter = 0;
    $counter++;
    return $counter;
}


say next_counter();
say next_counter();
say next_counter();

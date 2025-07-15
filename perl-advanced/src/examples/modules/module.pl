#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/modules';

require Calc;

print Calc::add(3, 4), "\n";

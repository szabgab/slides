#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/modules';

use B::Calc qw(add);

print add(2, 3), "\n";

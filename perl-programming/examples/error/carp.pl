#!/usr/bin/perl
use strict;
use warnings;

use Module;

Module::f("x");  # Parameter needs to be a number at Module.pm line 10.

Module::g("x");  # Parameter needs to be a number at carp.pl line 8

Module::h("x");
# Parameter needs to be a number at Module.pm line 24
#        Module::h('x') called at carp.pl line 9
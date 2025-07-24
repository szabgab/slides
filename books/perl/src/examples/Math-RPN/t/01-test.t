#!/usr/bin/perl
use strict;
use warnings;

use Test::More tests => 1;

use Math::RPN;

is rpn("1,1,+"), 2;

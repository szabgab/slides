#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib $FindBin::Bin;
use Compute qw(add);

print add(2, 3), "\n";


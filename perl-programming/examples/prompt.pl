#!/usr/bin/perl
use strict;
use warnings;

use IO::Prompt;

my $val = prompt 'Enter your choice [1,2,3]: ', 
                 -onechar,
                 -require=>{'Must be 1, 2 or 3' => qr/[123]/ };

print $val;

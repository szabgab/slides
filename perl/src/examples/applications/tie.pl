#!/usr/bin/env perl
use strict;
use warnings;

use Tie::File;

tie my @file, 'Tie::File', "data.txt" or die $!;
$file[7] = "Hello";


#!/usr/bin/perl
use strict;
use warnings;

use Pipe;

Pipe->find(".")->grep(qr/\.pl$/)->cat->grep(qr/perl/)->print("out.txt");


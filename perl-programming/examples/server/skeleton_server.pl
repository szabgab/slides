#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/lib";
use SkeletonServer;

SkeletonServer->run(port => 8000);

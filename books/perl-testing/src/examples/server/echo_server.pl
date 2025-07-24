#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/lib";
use EchoServer;

EchoServer->run(port => 8000);

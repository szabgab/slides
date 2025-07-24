#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/lib";
use SimpleEchoServer;

SimpleEchoServer->run(port => 8000);

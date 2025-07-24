#!/usr/bin/perl -w 
use strict;

use FindBin;
use lib "$FindBin::Bin/../lib";
use CLIDaemon;
use Getopt::Long qw(GetOptions);

my $port = 8000;
my $stderr;

GetOptions(
    "port=i" => \$port,
    "stderr" => \$stderr,
) or die "Usage $0 [--port PORT] [--stderr]\n";

if ($stderr) {
    close STDERR;
    open STDERR, ">stderr";
}

CLIDaemon->run(port => $port);


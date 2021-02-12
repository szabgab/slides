#!/usr/bin/env perl
use strict;
use warnings;

print "kill -15 $$    or press Ctrl-C    to stop\n";
my $continue = 1;
$SIG{TERM} = sub {
    print "TERM received\n";
    $continue = 0;
};

$SIG{INT} = sub {
    print "INT received\n";
    $continue = 0;
};

while ($continue) {
    if (open my $fh, '>>', 'process.log') {
        print $fh scalar localtime();
        print $fh "\n";
    }
    sleep 1;
}


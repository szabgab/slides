#!/usr/bin/env perl
use strict;
use warnings;

$SIG{KILL} = sub {
   print "KILL received. kill -9  We cannot catch it.\n";
};

$SIG{INT} = sub {
    print "INT received. kill -2  or Ctrl-C\n";
};

$SIG{TERM} = sub {
    print "TERM received. kill -15\n";
};

$SIG{TSTP} = sub {
    print "TSTP received. kill -20 or Ctrl-Z\n";
};

print "Please press Ctrl-C or Ctrl-Z\n";
print "(or type   kill -15 $$   on the command line)\n";

for my $i (1..100) {
    sleep 1;
    print "$i\n";
}
print "done\n";



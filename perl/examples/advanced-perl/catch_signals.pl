#!/usr/bin/perl 
use strict;
use warnings;

$SIG{KILL} = sub {
   print "KILL received\n";
};

$SIG{INT} = sub { 
    print "INT received\n";
};

$SIG{TERM} = sub {
    print "TERM received\n";
};

$SIG{TSTP} = sub {
    print "TSTP received\n";
};

print "Please press Ctrl-C or Ctrl-Z\n";
print "(or type   kill -15 $$   on the command line)\n";

for my $i (1..100) {
    sleep 1;
    print "$i\n";
}
print "done\n";



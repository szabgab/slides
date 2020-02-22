#!/usr/bin/perl 
use strict;
use warnings;


my $ctrl_c;

$SIG{INT} = sub { 
    if ($ctrl_c) {
        die "Ctrl-C received twice\n";
    }
    $ctrl_c++;
    print "Please, press Ctr-C again if you really mean it\n";
};

print "Please press Ctrl-C to terminate this program:\n";
for my $i (1..10) {
    sleep 1;
    print "$i\n";
}
print "done\n";

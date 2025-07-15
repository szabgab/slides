#!/usr/bin/env perl
use strict;
use warnings;

my $ctrl_c = 0;

$SIG{INT} = sub {
    if ($ctrl_c) {
        print "\nCtrl-C received twice\n";
        exit();
    }
    $ctrl_c++;
    print "\nPlease, press Ctr-C again if you really mean it\n";
};

print "Please press Ctrl-C to terminate this program:\n";
my $i = 0;
while (1) {
    $i++;
    print "$i\n";
    sleep 1;
}
print "done\n";

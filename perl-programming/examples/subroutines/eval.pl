#!/usr/bin/perl
use strict;
use warnings;


my $result;
my $x = 19;
my $y = 23;

eval {
    $result = unstable_add_function($x, $y);
    print "unstable done\n";
};
if ($@) {
    chomp $@;
    warn "Exception '$@' received\n";
    $result = slow_but_stable_add($x, $y);
    print "slow done\n";
}

print "Result: $result\n";
    


sub unstable_add_function {
    if (rand() < 0.2) {
        die "broken";
    }
    return $_[0]+$_[1];
}

sub slow_but_stable_add {
    sleep (2);
    return $_[0]+$_[1];
}

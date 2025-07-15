#!/usr/bin/env perl
use strict;
use warnings;

my $ctrl_c;

$SIG{INT} = sub {
        $ctrl_c = 1;
};

print "Please press Ctrl-C to terminate this program:\n";
for my $i (1..100) {
    confirm_exit();
    sleep 1;
    print "$i\n";
}
print "done\n";

sub confirm_exit {
    return if not $ctrl_c;

    local $SIG{INT} = 'IGNORE';

    $ctrl_c = 0;
    print "Do you really want to terminate the application? (y/n) [n]";
    chomp(my $input = <STDIN>);
    exit if $input eq 'y' or $input eq 'Y';
}


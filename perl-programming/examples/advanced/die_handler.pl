#!/usr/bin/perl 
use strict;
use warnings;

$SIG{__DIE__}  = sub { logger('error', $_[0]); };


print "Before\n";
die 'Something bad';
print "After\n";



sub logger {
    my ($level, $msg) = @_;
    if (open my $out, '>>', 'log.txt') {
        chomp $msg;
        print $out "$level - $msg\n";
    }
}

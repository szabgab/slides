#!/usr/bin/perl
use strict;
use warnings;

open my $ph, '|-', 'grep Perl ' or die "Cannot start process";
print $ph "aa\n";
print $ph "Perl was here\n";
print $ph "bb\n";
print $ph "ccPerl\n";
close $ph;


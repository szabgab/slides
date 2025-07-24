#!/usr/bin/perl
use strict;
use warnings;

my @ips = (
    '1.1.1.1',
    '1.1.1.1.5',
    '113412.1.1.1.5',
);

my $v0_199   = qr/1?\d?\d/;  # 0-199
my $v200_249 = qr/2[0-4]\d/; # 200-249  
my $v250_255 = qr/25[0-5]/;  # 250-255 

my $p = qr/$v0_199|$v200_249|$v250_255/;


foreach my $ip (@ips) {
    if ($ip =~ /$p\.$p\.$p\.$p/) {
        print "IP: $ip MATCH: $&\n";
    } else {
        print "IP: $ip NO match\n";
    }
}


print "----------\n";
IP: foreach my $ip (@ips) {
    if ($ip =~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/) {
        foreach my $v ($1, $2, $3, $4) {
            next IP if $v < 0 or $v > 255;
        }
        print "IP: $ip\n";
    }
}


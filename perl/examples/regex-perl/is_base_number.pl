#!/usr/bin/perl
use strict;
use warnings;

while (my $number = <STDIN>) {
    if (is_hex($number)) {
        print "Hexadecimal number\n";    # 0xAD37F
    }
    if (is_octal($number)) {
        print "Octal number\n";          # 02432471
    }
    if (is_binary($number)) {
        print "Binary number\n";         # 0b01110
    }
}

sub is_hex    { $_[0] =~ /^0x[\da-fA-F]+$/ }
sub is_octal  { $_[0] =~ /^0[0-7]+$/       } 
sub is_binary { $_[0] =~ /^0b[01]+$/       }

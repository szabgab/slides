#!/usr/bin/perl
use strict;
use warnings;


my $str = "hello world";
$str =~ /(..)/;
print "$1\n";
$str =~ /(..)\1/;   # unsuccessful matching does NOT reset $1
print "$1\n";

# $1 is localized, within blocks
{
	$str =~ /(.)\1/;
	print "$1\n";
}

print "$1\n"; # the same as earlier, before the {}

# any successful regular expression (even if it does not have capturing ())
# resets $1
$str =~ /./;  
print "$1\n";  # undef
	

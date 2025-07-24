#!/usr/bin/perl
use strict;
use warnings;

my $line = <STDIN>;
chomp $line;

my $first_space = index($line , " ");
my $first = substr($line, 0, $first_space);

my $last_space = rindex($line , " ");
my $second = substr($line, $last_space+1);


if (0 < index($line, "*")) {
	print $first * $second, "\n";
}
if (0 < index($line, "+")) {
	print $first + $second, "\n";
}

# optionally we could have fetched the part of the operator
# (possibly including a few additional spaces on either sides of it)
# $op = substr($line, $first_space+1, $last_space-$first_space-1);
# then we could use this in the if() statements instead of the $line


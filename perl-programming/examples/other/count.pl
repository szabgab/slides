#!/usr/bin/perl
use strict;
use warnings;

my %count;

while (my $line = <DATA>) {
	chomp $line;
	#print $line;
	my ($date, $channel, $action, $comment) = split /,/, $line;
	if ($date ne "20070127") {
		next;
	}
	$count{$action}++;
	#print "$date $action\n";
}

foreach my $action (keys %count) {
	print "$action   $count{$action}\n";
}


__DATA__
20070127,0245,drop,some comment
20070127,0245,search,some comment
20070126,0245,search,some comment
20070127,0246,search,some comment

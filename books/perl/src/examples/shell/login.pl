#!/usr/bin/perl
use strict;
use warnings;

# login.pl - mockup for login process

my $timeout=5;

while (1) {
	print "Username: ";                            # ask for the password and read it
	my $username = <STDIN>;
	chomp($username);
	my $pw;
	print "Password (within $timeout seconds): ";

	eval {                                         # read the password in a safe environment
		$SIG{ALRM} = sub {die("TIMEOUT\n")};   # setup the alarm handle routine
		alarm($timeout);                       # set the alarm clock
		$pw=<STDIN>;
		alarm(0);                              # reset the alarm clock
	};
	$SIG{ALRM} = 'DEFAULT';
	if ($@ =~ /^TIMEOUT$/) {
		alarm(0);                              # reset the alarm clock
		print "\nTime is over\n\n";
	} else {
		chomp($pw);
		last if check_password($username, $pw);
	}
}

sub check_password {
	my ($username, $pw) = @_;
	print "\nYou have entered $username/$pw now it is time to check them\n\n";
}

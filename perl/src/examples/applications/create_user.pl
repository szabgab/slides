#!/usr/bin/env perl
use strict;
use warnings;

# --fname Foo --lname Bar
# /usr/sbin/adduser --home /opt/bfoo --gecos "Foo Bar" bfoo

my $adduser = '/usr/sbin/adduser';

use Getopt::Long qw(GetOptions);

if (not @ARGV) {
    usage();
}

my %opts;
GetOptions(\%opts,
    'fname=s',
    'lname=s',
    'run',
) or usage();

if (not $opts{fname} or $opts{fname} !~ /^[a-zA-Z]+$/) {
    usage("First name must be alphabetic");
}
if (not $opts{lname} or $opts{lname} !~ /^[a-zA-Z]+$/) {
    usage("Last name must be alphabetic");
}
my $username = lc( substr($opts{lname}, 0, 1) . $opts{fname});
my $home     = "/opt/$username";

print "Username: $username\n";

my $cmd = qq($adduser --home $home --gecos "$opts{fname} $opts{lname}" $username);

print "$cmd\n";
if ($opts{run}) {
    system $cmd;
} else {
    print "need to add the --run flag to actually execute\n";
}


sub usage {
    my ($msg) = @_;
    if ($msg) {
        print "$msg\n\n";
    }
    print "Usage: $0 --fname FirstName --lname LastName --run\n";
    exit;
}

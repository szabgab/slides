#!/usr/bin/perl -w
use strict;
use Net::SNMP;

my $host = '10.202.156.240';
my $community = 'public';

my $session = Net::SNMP->session(
    -hostname  => $host,
    -community => $community,
) or die "Could not open session\n";

#'rsWSDLicense'

my $result = $session->get_request(
    -varbindlist => ['1.3.6.1.2.1.2.2.1.3.21'],
);

#my $result = $session->get_table(
#    -baseoid => '1.3.6.1.2.1.2.2.1.3',
#);

use Data::Dumper;
if ($result) {
    print "$result\n";
    print Dumper $result;
} else {
    print "NO result\n";
}

$session->close;

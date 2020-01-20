#!/usr/bin/perl 
use strict;
use warnings;

use Net::Pcap;
use Data::Dumper;
#print $Net::Pcap::VERSION;

# See also: http://www.perlmonks.org/index.pl?node_id=170648
#

my $err;
my $dev = Net::Pcap::lookupdev(\$err);
if ($err) {
    print "Error: $err\n";
}
if ($dev) {
    print "Device: $dev\n";
}

$err = undef;
my ($net, $mask);
Net::Pcap::lookupnet($dev, \$net, \$mask, \$err);
print "Net: $net\n";
print "Mask: $mask\n";

my $snaplen = 100;
my $promisc = 1;
my $to_ms = 0;
my $object = Net::Pcap::open_live($dev, $snaplen, $promisc, $to_ms, \$err);

my $count = 1;
my $user_data;
Net::Pcap::loop($object, $count, \&callback_function, $user_data);

sub callback_function {
    my ($user_data, $header, $packet) = @_;
    print Dumper $header;
}

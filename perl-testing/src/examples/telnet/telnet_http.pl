#!/usr/bin/perl
use strict;
use warnings;

my $CRLF = "\015\012";

use Net::Telnet ();
my $t = Net::Telnet->new(
    Binmode => 1,
    Timeout => 10,
    Host    => 'localhost',
    Port    => 5000,
);
 
$t->print("GET / HTTP/1.0$CRLF$CRLF") or die $!;
while (my $line = $t->getline) {
    print $line;
}
print "\n";

#!/usr/bin/perl
use strict;
use warnings;

use IO::Socket;

my $host = 'localhost';
my $port = 5000;
my $CRLF = "\015\012";

my $socket = IO::Socket::INET->new(
            PeerAddr => $host,
            PeerPort => $port,
            Proto    => 'tcp',
        ) or die $!;

$socket->send("GET / HTTP/1.0$CRLF$CRLF") or die $!;

my $SIZE = 100;
my $data = '';
while ($socket->read($data, $SIZE, length $data) == $SIZE) {};
print $data;
print "\n";

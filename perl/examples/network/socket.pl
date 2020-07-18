#!/usr/bin/perl
use strict;
use warnings;

use Socket qw(:DEFAULT :crlf);

# get the protocol id (on Linux from /etc/protocols)
my $protocol_id     = getprotobyname('tcp');  
socket(my $socket, PF_INET, SOCK_STREAM, $protocol_id) or die $!;


# build C structure in_addr from hostip
# if hostname is given it tries to resolve hostname to ip first
# (and returns undef if not successful)
my $host = 'localhost';
my $port   = 5000;
my $host_struct = inet_aton($host);  
my $sockaddr_in = pack_sockaddr_in($port, $host_struct);


connect($socket, $sockaddr_in) or die $!;

# turn off buffering on the socket
{
    my $old = select($socket);
    $| = 1;
    select($old);
}

print $socket "GET / HTTP/1.0$CRLF$CRLF";

while (my $line = <$socket>) {
    print $line;
}
print "\n";

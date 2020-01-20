#!/usr/bin/perl
use strict;
use warnings;

use IO::Socket;
use Getopt::Long qw(GetOptions);

my $MAX_SIZE = 500;
my $port = 2000;

GetOptions(
    "port=s" => \$port,
) or die $!;

my $socket = IO::Socket::INET->new(
    Proto => 'udp',
    LocalPort => $port,
) or die $@;

;

warn "UDP Echo service started on port $port\n";
while (1) {
    my $msg_in;
    next if not $socket->recv($msg_in, $MAX_SIZE);
    my $peerhost = gethostbyaddr($socket->peeraddr, AF_INET) or $socket->peerhost;
    my $peerport = $socket->peerport;
    my $length   = length($msg_in);
    warn "Received $length bytes from [$peerhost:$peerport]\n";
    my ($payload, $end) = mychomp($msg_in);
    my $msg_out = reverse($msg_in) . $end;
    $socket->send($msg_out) or die "send(): $!\n";
}
$socket->close;

# removing possible line ending newlines (carrig returns and line feeds)
sub mychomp {
    my ($str) = @_;
    my $end = '';
    if ($str =~ s/([\r\n]+)\z//) {
        $end = $1;
    }
    return ($str, $end);
}



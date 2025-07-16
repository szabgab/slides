#!/usr/bin/perl
use warnings;
use strict;

BEGIN {
    die "POE::Component::Client::Ping requires root privilege\n"
      if $> and ( $^O ne 'VMS' );
}

use POE;
use POE::Component::Client::Ping;

# How many seconds to wait for ping responses.
sub PING_TIMEOUT () { 5 }

#------------------------------------------------------------------------------
# A bunch of addresses to ping, culled from random NMIDA-infected web
# servers that have visited my dialup machine at one time or another.

my @xaddresses =
  qw( 10.0.0.0
  200.44.157.163 200.44.157.164 200.44.157.165 200.44.157.166
  206.1.2.254 206.103.218.217 206.111.218.76 206.111.75.28
  206.126.248.4 206.137.229.4 206.152.242.14 206.156.108.156
  206.156.157.83 206.167.114.118 206.167.114.119 206.167.44.49
  206.167.44.81 206.191.88.39 206.205.253.20 206.208.187.11
  206.211.137.26 206.215.127.204 206.222.52.70 206.252.204.14
  206.254.1.139 206.254.217.101 206.28.58.186 206.40.164.34
  206.45.180.82 206.48.59.156 206.50.127.17 206.58.130.120
  206.83.86.132 206.86.239.12 24.15.162.192 65.107.88.167
);

my @addressex =
    qw(127.0.0.1
);

#------------------------------------------------------------------------------
# The main loop.

# Create a pinger component.  This will do the work of multiple
# concurrent pings.  It requires another session to interact with it.

POE::Component::Client::Ping->spawn
  ( Alias => 'pinger',    # The component's name will be "pinger".
    Timeout => PING_TIMEOUT,    # The default ping timeout.
  );

# Create a session that will use the pinger.  Its parameters match
# event names with the functions that will handle them.

POE::Session->create
  ( inline_states =>
      { _start => \&client_start,    # Call client_start() to handle "_start".
        pong => \&client_got_pong,    # Call client_got_pong() to handle "pong".
      }
  );

# Start POE's main loop.  It will only return when everything is done.

$poe_kernel->run();
exit;

#------------------------------------------------------------------------------
# Event handlers.

# Handle _start (given by POE itself to start your session) by sending
# several "ping" commands to the component at once.  The component
# will reply over the course of PING_TIMEOUT seconds.

sub client_start {
    my ( $kernel, $session ) = @_[ KERNEL, SESSION ];

    print "Starting to ping hosts.\n";

    foreach my $address (@addresses) {
        print "Pinging $address at ", scalar(localtime), "\n";

        # "Pinger, do a ping and return the results as a pong event.  The
        # address to ping is $ping."

        $kernel->post( pinger => ping => pong => $address );
    }
}

# Handle a "pong" event (returned by the Ping component because we
# asked it to).  Just display some information about the ping.

sub client_got_pong {
    my ( $kernel, $session ) = @_[ KERNEL, SESSION ];

    # The original request is returned as the first parameter.  It
    # contains the address we wanted to ping, the total time to wait for
    # a response, and the time the request was made.

    my $request_packet = $_[ARG0];
    my ( $request_address, $request_timeout, $request_time ) = @{$request_packet};

    # The response information is returned as the second parameter.  It
    # contains the response address (which may be different from the
    # request address), the ping's round-trip time, and the time the
    # reply was received.

    my $response_packet = $_[ARG1];
    my ( $response_address, $roundtrip_time, $reply_time ) = @{$response_packet};

    # It is impossible to know ahead of time how many ICMP ping
    # responses will arrive for a particular address, so the component
    # always waits PING_TIMEOUT seconds.  An undefined response address
    # signals that this waiting period has ended.

    if ( defined $response_address ) {
        printf( "Pinged %-15.15s - Response from %-15.15s in %6.3fs\n",
            $request_address, $response_address, $roundtrip_time
        );
    }
    else {
        print "Time's up for responses from $request_address.\n";
    }
}

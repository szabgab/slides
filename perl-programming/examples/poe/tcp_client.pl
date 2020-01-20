#!/usr/bin/perl
use strict;
use warnings;

use POE;
use POE::Component::Client::TCP;
use POE::Filter::Stream;

my @ports = qw( pop3 smtp nntp http imap3 );    # The ports to connect to.
my $host  = "localhost";                        # The host to test.

# Spawn a new client for each port.

foreach my $port (@ports) {

    POE::Component::Client::TCP->new
      ( RemoteAddress => $host,
        RemotePort => $port,
        Filter     => "POE::Filter::Stream",

        # The client has connected.  Display some status and prepare to
        # gather information.  Start a timer that will send ENTER if the
        # server does not talk to us for a while.

        Connected => sub {
            print "connected to $host:$port ...\n";
            $_[HEAP]->{banner_buffer} = [];
            $_[KERNEL]->delay( send_enter => 5 );
        },

        # The connection failed.

        ConnectError => sub {
            print "could not connect to $host:$port ...\n";
        },

        # The server has sent us something.  Save the information.  Stop
        # the ENTER timer, and begin (or refresh) an input timer.  The
        # input timer will go off if the server becomes idle.

        ServerInput => sub {
            my ( $kernel, $heap, $input ) = @_[ KERNEL, HEAP, ARG0 ];
            print "got input from $host:$port ...\n";
            push @{ $heap->{banner_buffer} }, $input;
            $kernel->delay( send_enter    => undef );
            $kernel->delay( input_timeout => 1 );
        },

        # These are handlers for additional events not included in the
        # default Server::TCP module.  In this example, they handle
        # timers that have gone off.

        InlineStates =>
          {    # The server has not sent us anything yet.  Send an ENTER
                # keystroke (really a network newline, \x0D\x0A), and wait
                # some more.

            send_enter => sub {
                print "sending enter on $host:$port ...\n";
                $_[HEAP]->{server}->put("");    # sends enter
                $_[KERNEL]->delay( input_timeout => 5 );
            },

            # The server sent us something already, but it has become idle
            # again.  Display what the server sent us so far, and shut
            # down.

            input_timeout => sub {
                my ( $kernel, $heap ) = @_[ KERNEL, HEAP ];

                print "got input timeout from $host:$port ...\n";
                print ",----- Banner from $host:$port\n";
                foreach ( @{ $heap->{banner_buffer} } ) {
                    print "| $_";

                    # print "| ", unpack("H*", $_), "\n";
                }
                print "`-----\n";

                $kernel->yield("shutdown");
            },
          },
      );
}

# Run the clients until the last one has shut down.

$poe_kernel->run();
exit 0;

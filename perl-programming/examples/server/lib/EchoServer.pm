package EchoServer;
use warnings;
use strict;

use base 'Net::Server';
use English qw( -no_match_vars ) ;

my $timeout = 5; # give the user 5 seconds to type a line
my $EOL   = "\015\012";

sub process_request {
    my $self = shift;
    print "Welcome to the echo server$EOL";
    print "Type 'bye' to disconnect.$EOL";
    eval {

        local $SIG{ALRM} = sub { die "Timeout\n" };

        alarm($timeout);
        while( my $line = <STDIN> ) {
            alarm($timeout);
            $line =~ s/\r?\n$//;
            print qq(You said "$line"$EOL);
            last if $line eq "bye";
        }
    };
    alarm(0);

    
    if ( $EVAL_ERROR ) {
        if ( $EVAL_ERROR eq "Timeout\n" ) {
            print "Timed Out. Disconnecting...$EOL";
            print STDERR "Client timed Out.\n";
        } else {
            print "Unknown internal error. Disconnecting...$EOL";
            print STDERR "Unknown internal error: $EVAL_ERROR\n";
        }
    } else {
        print STDERR "User said bye\n";
    }
    return;
}



1;


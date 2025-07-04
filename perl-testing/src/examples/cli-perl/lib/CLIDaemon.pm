package CLIDaemon;
use warnings;
use strict;
use 5.008;

our $VERSION = '0.01';

use base 'Net::Server::PreFork';
my $EOL   = "\015\012";

use CLIDaemon::Connection;
use CLIDaemon::Server;

my $server;
my $timeout = 30;

sub process_request {
    my $self = shift;
    if (not $server) {
        $server = CLIDaemon::Server->new;
    }
    eval {

        local $SIG{ALRM} = sub { die "Timed Out!\n" };

        alarm($timeout);
        my $c = CLIDaemon::Connection->new();
        print "Welcome$EOL";
        $c->prompt();
        while( my $input = <STDIN> ){
            $input =~ s/\r?\n$//;

            if ($c->state eq "username") {
                $c->username($input);
                $c->state("password");
                $c->prompt();
            } elsif ($c->state eq "password") {
                $c->password($input);
                if ($server->good_login($c->username, $c->password)) {
                    $c->state("basic");
                    $c->prompt();
                } else {
                    print "Invalid login$EOL";
                    $c->state("username");
                    $c->prompt(); 
                }
            } elsif ($c->state eq "basic") {
                # BUG not always gives prompt (if should not be here)
                if ($server->process_basic($input)) {
                    $c->prompt(); 
                }
            } elsif ($c->state eq "enabled") {
                $server->process_enabled($input);
                $c->prompt();
            } else {
                printf STDERR "Invalid state: '%s'", $c->state;
            }

            alarm($timeout);
        }

    };
    alarm(0);

    if ( $@ =~ /Timed Out/ ) {
        print "Timed Out.$EOL";
        return;
    } elsif ( $@ =~ /EXIT/ ) {
        print STDERR "Normal exit\n";
        return;
    }
}

1;


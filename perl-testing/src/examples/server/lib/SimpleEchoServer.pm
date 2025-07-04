package SimpleEchoServer;
use warnings;
use strict;

use base 'Net::Server';
my $EOL   = "\015\012";

sub process_request {
    my $self = shift;
    while( my $line = <STDIN> ) {
        $line =~ s/\r?\n$//;
        print qq(You said "$line"$EOL);
        last if $line eq "bye";
    }
}

1;

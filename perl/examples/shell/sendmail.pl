#!/usr/bin/perl
use strict;
use warnings;

sendmail('Info <info@perlmaven.com>',
    'hello world',
    'text...',
    'Noreply <noreply@perlmaven.com>');

sub sendmail {
    my ($tofield, $subject, $text, $fromfield) = @_;
    my $mailprog = "/usr/lib/sendmail";

    open my $ph, '|-', "$mailprog -t -oi" or die $!;
    print $ph "To: $tofield\n";
    print $ph "From: $fromfield\n";
    print $ph "Reply-To: $fromfield\n";
    print $ph "Subject: $subject\n";
    print $ph "\n";
    print $ph "$text";
    close $ph;
    return ;
}

# Warning: do not use the above script in an environment
# where anyone can supply the fields in the header
# (To, From, Reply-To, Subject in this case)
# as this can create an open relay.


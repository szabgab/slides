#!/usr/bin/perl
use strict;
use warnings;

use Expect;
my $e = Expect->new;
#$e->debug(3);
$e->raw_pty(1);
#$e->log_file("ssh.log", "w");
$e->spawn("ssh localhost") or die "Could not start ssh ac\n";
$e->expect(2, '[gabor@gabor ~]$') or die "Could not connect\n";
$e->send("date\n");  # Wed Jul 28 23:00:43 IDT 2004
$e->expect(1, '[gabor@gabor ~]$') or die "No prompt\n";
$e->send("who\n");
$e->expect(1, '[gabor@gabor ~]$') or die "No prompt\n";
#save("who.txt", $e->before);

print "\n";
# gabor    pts/0        Jul 28 20:58 (l192-115-61-144.tcable.actcom.net.il)
# gabor    pts/1        Jul 28 22:59 (l192-115-61-144.tcable.actcom.net.il)
# You have new mail in /var/spool/mail/gabor
# [gabor@ac gabor]$ 


# uptime
#  23:02:57  up  2:28,  2 users,  load average: 0.17, 0.12, 0.09
#

# ps axuw - check if a certain process is runnig or not
# maybe change the configuration file of the 

sub save {
    my ($filename, $text) = @_;
    open my $fh, ">", $filename or die;
    print $fh $text;
}


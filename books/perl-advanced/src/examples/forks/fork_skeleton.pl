use strict;
use warnings;

main();

sub main {
    my $pid = fork();
    die "Could not fork" if not defined $pid;

    if (not $pid) {
        print "In child process\n";
        exit;
    }

    print "In parent process\n";
    my $finished = wait();
}


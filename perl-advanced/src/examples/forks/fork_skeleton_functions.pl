use strict;
use warnings;

main();

sub main {
    my $pid = fork();
    die "Could not fork" if not defined $pid;

    if ($pid) {
        parent_process();
    } else {
        child_process();
    }

}

sub child_process {
    print "In child process\n";
    exit;
}

sub parent_process {
    print "In parent process\n";
    my $finished = wait();
}

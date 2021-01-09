use strict;
use warnings;

main();

sub main {
    my $pid = fork();
    die "Could not fork" if not defined $pid;
    if (not $pid) {
        sleep 1;
        my $parent = getppid();
        print "In Child:  PID: $$ from parnet: $parent\n";;
        exit;
    }
    sleep 1;
    print "In Parent: PID: $$ Child: $pid\n";
    my $finished = wait();
    my $exit_code = $? / 256;
    print "Child finised: $finished Exit code: $exit_code\n";
}


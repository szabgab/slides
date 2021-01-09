use strict;
use warnings;
use Time::HiRes qw(time);
use lib '.';
use Task;

main();


sub main {
    my ($forks) = @ARGV;
    die "Usage: $0 FORKS\n" if not $forks;

    for my $id (1 .. $forks) {
        my $pid = fork();
        die "Could not fork" if not defined $pid;
        if (not $pid) {
            sleep 1;
            my $parent = getppid();
            print "Fork number $id, In Child:  PID: $$ from parnet: $parent\n";;
            exit;
        }
        print "In Parent: PID: $$ Child created: $pid\n";
    }
    sleep 1;
    print "In Parent: PID: $$\n";
    for (1 .. $forks) {
        my $finished = wait();
        my $exit_code = $? / 256;
        print "Child finised: $finished with exit code $exit_code\n";
    }
}


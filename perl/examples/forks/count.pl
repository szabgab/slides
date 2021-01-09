use strict;
use warnings;
use Time::HiRes qw(time);
use lib '.';
use Task;

main();


sub main {
    my ($fork_count, $task_count, $max) = @ARGV;
    die "Usage: $0 FORK_COUNT HOW_MANY_TIMES TILL_WHICH_NUMBER\n" if not $max;
    my $start = time;

    if ($fork_count == 0) {
        for my $i (1..$task_count) {
            Task::count($max);
        }
    } else {
        my @tasks;
        push @tasks, 1+int($task_count/$fork_count) for 1 .. ($task_count % $fork_count);
        push @tasks, int($task_count/$fork_count) for 1 .. ($fork_count - ($task_count % $fork_count));
        print "@tasks\n";
        for my $fork_id (1 .. $fork_count) {
            my $pid = fork();
            die "Could not fork" if not defined $pid;
            if (not $pid) {
                #print "PID $pid $tasks[$fork_id-1]\n";
                for my $i (1..$tasks[$fork_id-1]) {
                    Task::count($max);
                    print "done\n";
                }
                exit;
            }
        }
        for my $fork_id (1 .. $fork_count) {
            wait();
        }
    }


    my $end = time;
    my $elapsed = $end-$start;
    print "Elapsed time $elapsed\n";
}



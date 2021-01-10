package ForkedCounter;
use strict;
use warnings;
use Task;


sub counter_one_by_one {
    my ($task_count, $max) = @_;

    for my $fork_id (1 .. $task_count) {
        my $pid = fork();
        die "Could not fork" if not defined $pid;
        if (not $pid) {
            Task::count($max);
            exit;
        }
    }
    for my $fork_id (1 .. $task_count) {
        wait();
    }
}


sub counter {
    my ($fork_count, $task_count, $max) = @_;

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
            }
            exit;
        }
    }
    for my $fork_id (1 .. $fork_count) {
        wait();
    }
}

1;

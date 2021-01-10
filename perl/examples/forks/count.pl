use strict;
use warnings;
use Time::HiRes qw(time);
use lib '.';
use Task;
use ForkedCounter;

main();


sub main {
    my ($fork_count, $task_count, $max) = @ARGV;
    die "Usage: $0 FORK_COUNT HOW_MANY_TIMES TILL_WHICH_NUMBER\n" if not $max;
    my $start = time;

    if ($fork_count == 0) {
        for my $i (1..$task_count) {
            Task::count($max);
        }
    } elsif ($fork_count == -1) {
        ForkedCounter::counter_one_by_one($task_count, $max);
    } else {
        ForkedCounter::counter($fork_count, $task_count, $max);
    }


    my $end = time;
    my $elapsed = $end-$start;
    printf "Elapsed time %.2f\n", $elapsed;
}



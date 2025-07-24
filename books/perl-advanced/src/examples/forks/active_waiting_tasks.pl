use strict;
use warnings;
use Time::HiRes qw(sleep);
use POSIX ':sys_wait_h';

main();

sub main {
    my ($workers) = @ARGV;
    die "Usage: $0 WORKERS\n" if not defined $workers;
    #my @tasks = 'a' .. 'z';
    my @tasks = 'a' .. 'd';

    my %process;
    while (1) {
        if (@tasks and scalar(keys %process) < $workers) {
            my $task = shift @tasks;

            my $pid = fork();
            die 'Failed to fork' if not defined $pid;

            if ($pid == 0) {
                my $exit_code = int rand(3);
                my $sleep_time = rand(5);
                print "Child process Task: $task PID $$ will sleep for $sleep_time and then exit with code $exit_code\n";
                sleep $sleep_time;
                exit $exit_code;
            }
            $process{$pid} = $task;
            next;
        }

        my $pid = waitpid(-1, WNOHANG);
        if ($pid > 0) {
            my $exit_code = $?/256;
            my $task = delete $process{$pid};
            print "Child process $pid task $task finished with exit code $exit_code\n";
            if ($exit_code > 0) {
                unshift @tasks, $task;
            }
            next;
        }
        sleep 0.1;
        last if not %process;
    }
}

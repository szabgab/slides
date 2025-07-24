use strict;
use warnings;
use Time::HiRes qw(sleep);
use POSIX ':sys_wait_h';

main();

sub main {
    my ($workers) = @ARGV;

    die "Usage: $0 WORKERS\n" if not defined $workers;
    $| = 1; # disable output buffering on STDOUT

    my %process;
    for my $worker_id (1 .. $workers) {
        my $pid = fork();
        die 'Failed to fork' if not defined $pid;

        if ($pid == 0) {
            my $exit_code = int rand(5);
            my $sleep_time = rand(5);
            print "Child process worker ID: $worker_id  PID $$ will sleep for $sleep_time and then exit with code $exit_code\n";
            sleep $sleep_time;
            exit $exit_code;
        }
        $process{$pid} = $worker_id;
        next;
    }

    while (1) {
        my $pid = waitpid(-1, WNOHANG);
        if ($pid > 0) {
            my $exit_code = $?/256;
            my $worker_id = delete $process{$pid};
            print "Child process $pid worker id $worker_id finished with exit code $exit_code\n";
            next;
        }
        print '.';
        sleep 0.1;
        last if not %process;
    }
}

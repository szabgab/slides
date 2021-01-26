use strict;
use warnings;
use Time::HiRes qw(sleep);

use POSIX ':sys_wait_h';

main();

sub main {
    my ($sleep, $exit) = @ARGV;

    die "Usage: $0 SLEEP EXIT\n" if not defined $exit;

    my $pid = fork();
    die 'Failed to fork' if not defined $pid;

    if ($pid == 0) {
        print "Child process PID $$\n";
        sleep $sleep;
        exit $exit;
    }

    while (1) {
        my $pid = waitpid(-1, WNOHANG);
        if ($pid > 0) {
            my $exit_code = $?/256;
            print "Child process $pid finished with exit code $exit_code\n";
            last;
        }
        print "Parent could do something else, but now sleeping\n";
        sleep 0.1;
    }
}

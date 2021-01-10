use strict;
use warnings;

my $historical = 42;
main();

sub main {
    print "PID before fork $$\n";
    my $pid = fork();
    die "Could not fork" if not defined $pid;

    if ($pid) {
        print "PID of child: $pid\n";
        parent_process();
    } else {
        print "PID received in child: $pid\n";
        child_process();
    }

}

sub child_process {
    #sleep 1;
    my $ppid = getppid();
    print "In child process $$ of parent $ppid\n";
    print "value in child: $historical\n";
    $historical = 23;
    #my $x = 0;
    #my $y = 3 / $x;
    #die "bad thing";
    exit 42;
}

sub parent_process {
    #sleep 1;
    print "value in parent $historical\n";
    my $ppid = getppid();
    print "In parent process $$ of parent $ppid\n";
    my $finished = wait();
    my $exit_code = $? / 256;
    print "finished: $finished\n";
    print "exit code: $exit_code\n";
    print "value in parent $historical\n";
}

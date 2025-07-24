use strict;
use warnings;

BEGIN {
    if ($^O eq "MSWin32") {
        print "Running on Windows\n";
        require Win32::Getppid;
        import Win32::Getppid qw(getppid);
    }
}

main();


sub main {
    my ($forks) = @ARGV;
    die "Usage: $0 FORKS\n" if not $forks;

    my $shared = 42;

    for my $id (1 .. $forks) {
        my $pid = fork();
        die "Could not fork" if not defined $pid;
        if (not $pid) {
            sleep 1;
            my $parent = getppid();
            print "Fork number $id, In Child:  PID: $$ from parnet: $parent\n";;
            print "Shared value: $shared\n";
            $shared = $$;
            exit;
        }
        print "In Parent: PID: $$ Child created: $pid\n";
    }
    sleep 1;
    print "In Parent: PID: $$\n";
    print "Shared value: $shared\n";
    for (1 .. $forks) {
        my $finished = wait();
        my $exit_code = $? / 256;
        print "Child finised: $finished with exit code $exit_code\n";
    }
}


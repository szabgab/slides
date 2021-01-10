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
    my $shared = 42;

    my $pid = fork();
    die "Could not fork" if not defined $pid;
    if (not $pid) {
        sleep 1;
        my $parent = getppid();
        print "In Child:  PID: $$ from parnet: $parent\n";;
        print "Shared value: $shared\n";
        $shared = $$;
        exit;
    }
    sleep 1;
    print "In Parent: PID: $$ Child: $pid\n";
    my $finished = wait();
    my $exit_code = $? / 256;
    print "Child finised: $finished Exit code: $exit_code\n";
    print "Shared: $shared\n";
}


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
    my $parent = getppid();
    print "PID: $$ from parnet: $parent\n";
}


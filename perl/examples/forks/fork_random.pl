use strict;
use warnings;

srand 42;
print rand(), "\n";
print rand(), "\n";
print rand(), "\n";
#exit;

main();

sub main {
    my $pid = fork();
    die "Could not fork" if not defined $pid;

    if ($pid) {
        parent_process();
    } else {
        child_process();
    }

}

sub child_process {
    #srand;
    print "In child process\n";
    print "child ", rand(), "\n";
    print "child ", rand(), "\n";
    print "child ", rand(), "\n";
    exit;
}

sub parent_process {
    print "In parent process\n";
    print "parent ", rand(), "\n";
    print "parent ", rand(), "\n";
    print "parent ", rand(), "\n";
    my $finished = wait();
}

use strict;
use warnings;

my $pid = fork();
die "Could not fork()\n" if not defined $pid;

if (not $pid) {
    # call the external implementation of the server
    # exec("bin/server.pl");

    # or implement the server inline here and then call exit();
    sleep(1000);
    exit(0);
}

# give the server a chance to start
sleep(1);


require Test::More;
import Test::More;

plan(tests => 1);

# start up the client code here
# and call the testing functions
ok(1);


END {
    # make sure the server gets killed even if the
    # test finishes abnornmally
    kill 9, $pid if $pid;
}


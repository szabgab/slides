use strict;
use warnings;

use MCE;

main();


sub main {
    my ($workers) = @ARGV;
    die "Usage: $0 WORKERS\n" if not defined $workers;

    my $mce = MCE->new(
        max_workers => $workers,
        user_func => sub {
            my ($mce) = @_;
            $mce->say("Hello from PID $$ WID " . $mce->wid);
        }
     );

    $mce->run;
}



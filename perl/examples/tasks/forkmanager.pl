use strict;
use warnings;
use Parallel::ForkManager;
use Data::Dumper qw(Dumper);

main();

sub main {
    my ($parallels) = @ARGV;
    die "Usage: $0 PARALLELS\n" if not defined $parallels;

    my $shared = 42;

    my $pm = Parallel::ForkManager->new($parallels);
    foreach my $input (2, 3, 5, 11) {
        my $pid = $pm->start and next;
        print "PID $$ input: $input shared: $shared\n";
        $shared = $$;
        $pm->finish();
    }
    $pm->wait_all_children;

    print "Shared: $shared\n";
}


use strict;
use warnings;
use Parallel::ForkManager;
use Data::Dumper qw(Dumper);

main();

sub main {
    my ($parallels) = @ARGV;
    die "Usage: $0 PARALLELS\n" if not defined $parallels;

    my %results;

    my $pm = Parallel::ForkManager->new($parallels);
    $pm->run_on_finish( sub {
        my ($pid, $exit_code, $ident, $exit_signal, $core_dump, $data_structure_reference) = @_;
        my $input = $data_structure_reference->{input};
        $results{$input} = $data_structure_reference->{result};
        #print "Finished PID $pid and exit code: $exit_code\n";
    });
    foreach my $input (2, 3, 5, 11) {
        my $pid = $pm->start and next;
        print "PID $$\n";
        my $result = $input * 2;
        $pm->finish(0, {input => $input, result => $result});
    }
    $pm->wait_all_children;

    print Dumper \%results;
}


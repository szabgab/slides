package ForkedProcessCSV;
use strict;
use warnings;
use Parallel::ForkManager;
use lib '.';
use Task;

sub process_csv {
    my ($parallels, @files) = @_;

    my %results;
    my $pm = Parallel::ForkManager->new($parallels);
    $pm->run_on_finish( sub {
        my ($pid, $exit_code, $ident, $exit_signal, $core_dump, $data_structure_reference) = @_;
        my $filename = $data_structure_reference->{filename};
        $results{$filename} = $data_structure_reference->{total};
        #print "Finished PID $pid and exit code: $exit_code\n";
    });
    foreach my $file (@files) {
        my $pid = $pm->start and next;
        print "PID $$\n";
        my $total = Task::process_file($file);
        $pm->finish(0, {filename => $file, total => $total});
    }
    $pm->wait_all_children;

    return %results;
}

1;




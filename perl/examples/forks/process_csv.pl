use strict;
use warnings;
use Time::HiRes qw(time);
use Parallel::ForkManager;
use lib '.';
use Task;

main();

sub main {
    my $parallels = shift @ARGV;
    my @files = @ARGV;
    my %results;
    #print "@files";
    my $start = time;
    if ($parallels == 0) {
        for my $file (@files) {
            my $total = Task::process_file($file);
            $results{$file} = $total;
        }
    } else {
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
    }

    for my $file (@files) {
        print "$file $results{$file}\n";
    }

    my $end = time;
    my $elapsed = $end-$start;
    print "Elapsed time $elapsed\n";
}

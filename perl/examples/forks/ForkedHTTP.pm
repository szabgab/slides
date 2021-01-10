package ForkedHTTP;
use strict;
use warnings;
use Parallel::ForkManager;
use lib '.';
use Task;

sub get_titles {
    my ($parallels, @urls) = @_;

    my %results;

    my $pm = Parallel::ForkManager->new($parallels);
    $pm->run_on_finish( sub {
        my ($pid, $exit_code, $ident, $exit_signal, $core_dump, $data_structure_reference) = @_;
        my $url = $data_structure_reference->{url};
        $results{$url} = $data_structure_reference->{title};
    });
    foreach my $url (@urls) {
        my $pid = $pm->start and next;
        print "PID $$\n";
        my $title = Task::get_title($url);
        $pm->finish(0, {url => $url, title => $title});
    }
    $pm->wait_all_children;

    return %results;
}

1;


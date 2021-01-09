use strict;
use warnings;
use LWP::Simple qw(get);
use Time::HiRes qw(time);
use HTML::TreeBuilder::XPath;
use Parallel::ForkManager;

binmode(STDOUT, ":utf8");

main();


sub get_title {
    my ($url) = @_;

    my $content = get $url;
    my $tree= HTML::TreeBuilder::XPath->new_from_content($content);
    my $nb = $tree->findvalue( '/html/head/title' );

    return $nb;
}

sub main {
    my ($filename, $parallels, $limit) = @ARGV;
    die "Usage: $0 FILENAME PARALLEL LIMIT\n" if not defined $limit;

    open my $fh, '<', $filename or die;
    my @urls = <$fh>;
    chomp @urls;
    if ($limit and $limit < scalar @urls) {
        @urls = @urls[0..$limit-1];
    }
    #print scalar @urls;

    my %results;
    my $start = time;
    if ($parallels == 0) {
        for my $url (@urls) {
            $results{$url} = get_title($url);
        }
    } else {
        my $pm = Parallel::ForkManager->new($parallels);
        $pm->run_on_finish( sub {
            my ($pid, $exit_code, $ident, $exit_signal, $core_dump, $data_structure_reference) = @_;
            my $url = $data_structure_reference->{url};
            $results{$url} = $data_structure_reference->{title};
        });
        foreach my $url (@urls) {
            my $pid = $pm->start and next;
            print "PID $$\n";
            my $title = get_title($url);
            $pm->finish(0, {url => $url, title => $title});
        }
        $pm->wait_all_children;

    }

    for my $url (@urls) {
        print "$url  $results{$url}\n";
    }

    my $end = time;
    my $elapsed = $end-$start;
    print "Elapsed time $elapsed\n";

}

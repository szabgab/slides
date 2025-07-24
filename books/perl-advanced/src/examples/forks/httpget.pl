use strict;
use warnings;
use Time::HiRes qw(time);
use lib '.';
use Task;
use ForkedHTTP;

binmode(STDOUT, ":utf8");

main();


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
            $results{$url} = Task::get_title($url);
        }
    } else {
        %results = ForkedHTTP::get_titles($parallels, @urls);
    }

    for my $url (@urls) {
        print "$url  $results{$url}\n";
    }

    my $end = time;
    my $elapsed = $end-$start;
    printf "Elapsed time %.2f\n", $elapsed;
}

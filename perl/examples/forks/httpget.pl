use strict;
use warnings;
use LWP::Simple qw(get);
use Time::HiRes qw(time);
use HTML::TreeBuilder::XPath;

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
    my ($filename, $limit) = @ARGV;
    die "Usage: $0 FILENAME LIMIT\n" if not defined $limit;
    open my $fh, '<', $filename or die;
    my @urls = <$fh>;
    chomp @urls;
    if ($limit and $limit < scalar @urls) {
        @urls = @urls[0..$limit-1];
    }
    #print scalar @urls;

    my %results;
    my $start = time;
    for my $url (@urls) {
        $results{$url} = get_title($url);
    }

    for my $url (@urls) {
        print "$url  $results{$url}\n";
    }

    my $end = time;
    my $elapsed = $end-$start;
    print "Elapsed time $elapsed\n";

}

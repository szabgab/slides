package Task;
use strict;
use warnings;
use Time::HiRes qw(time);
use LWP::Simple qw(get);
use HTML::TreeBuilder::XPath;

sub count {
    my ($max) = @_;

    my $start = time;

    my $counter = 0;
    while ($counter < $max) {
        $counter++;
    }

    my $end = time;
    my $elapsed = $end-$start;
    print "done in $elapsed\n";
}

sub process_file {
    my ($file) = @_;

    my $total = 0;
    open my $fh, '<', $file or die;
    while (my $line = <$fh>) {
        chomp $line;
        my @fields = split /,/, $line;
        $total += $fields[2];
    }

    return $total;
}

sub get_title {
    my ($url) = @_;

    my $content = get $url;
    my $tree= HTML::TreeBuilder::XPath->new_from_content($content);
    my $nb = $tree->findvalue( '/html/head/title' );

    return $nb;
}


1;
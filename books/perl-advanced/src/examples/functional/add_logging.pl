use strict;
use warnings;

sub count {
    my ($limit) = @_;
    print "count till $limit\n";
    my $counter = 0;
    $counter++ while $counter < $limit;
}

sub show_elapsed {
    my ($sub) = @_;

    use Time::HiRes qw(time);
    return sub {
        my $start = time;
        $sub->(@_);
        my $end = time;
        my $elapsed = $end - $start;
        print "Elapsed time: $elapsed\n";
    }
}

my $newcount = show_elapsed(\&count);
$newcount->(10000000);
#*count = $newcount;

count(10000000);


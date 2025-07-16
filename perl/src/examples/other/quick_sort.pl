use strict;
use warnings;
use 5.010;
use Benchmark qw(:hireswallclock);

my @numbers = (1 .. 4);
print "@numbers\n";
my @sorted = quick_sort(@numbers);
print "@sorted\n";

#timethese(1, {
#    '1000'   => sub { quick_sort(1..1000) },
#    '10000'  => sub { quick_sort(1..10000) },
#    '100000' => sub { quick_sort(1..100000) },
#});
#
#say(timeit(10, sub { quick_sort(1..1000)  })->real);

sub quick_sort {
    my @items = @_;
    #print "@items\n";
    if (scalar(@items) <= 1) {
        return @items;
    }
    my $pivot  = int(scalar(@items) / 2);  # this could be the first element or a random element.
    my @left  = grep { $_ > $items[$picot] } @items;
    my @right = grep { $_ < $items[$picot] } @items;
    my @same  = grep { $_ == $items[$picot] } @items;

    return quick_sort(@left), @same, quick_sort(@right);
}


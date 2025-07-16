use strict;
use warnings;
use 5.010;
use Benchmark qw(:hireswallclock);

my @numbers = (1 .. 4);
print "@numbers\n";
my @sorted = insert_sort(@numbers);
print "@sorted\n";

#timethese(1, {
#    '1000'  => sub { insert_sort(1..1000) },
#    '10000' => sub { insert_sort(1..10000) },
#});

#say(timeit(10, sub { insert_sort(1..1000)  })->real);

sub insert_sort {
    my @items = @_;
    for my $ix (1 .. $#items) {
        my $current_item = $items[$ix];
        my $jx = $ix - 1;
        while ($jx >= 0 and $current_item > $items[$jx]) {
            $items[$jx+1] = $items[$jx];
            $jx--;
        }
        $items[$jx+1] = $current_item;
        #print "@items\n";
    }
    return @items;
}

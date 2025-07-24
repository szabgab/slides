use strict;
use warnings;
use 5.010;
use Benchmark qw(:hireswallclock);

my @numbers = (1 .. 4);
print "@numbers\n";
my @sorted = bubble_sort(@numbers);
print "@sorted\n";

#timethese(1, {
#    '1000'  => sub { bubble_sort(1..1000) },
#    '10000' => sub { bubble_sort(1..10000) },
#});

#say(timeit(10, sub { bubble_sort(1..1000)  })->real);

sub bubble_sort {
    my @items = @_;
    for my $ix (0 .. $#items) {
        for my $jx (0 .. $#items-$ix-1) {
            if ($items[$jx] < $items[$jx+1]) {
                ($items[$jx], $items[$jx+1]) = ($items[$jx+1], $items[$jx]);
                print "@items\n";
            }
        }
    }
    return @items;
}

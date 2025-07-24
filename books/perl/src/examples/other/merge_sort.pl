use strict;
use warnings;
use 5.010;
use Benchmark qw(:hireswallclock);

my @numbers = (1 .. 4);
print "@numbers\n";
my @sorted = merge_sort(@numbers);
print "@sorted\n";

#timethese(1, {
#    '1000'   => sub { merge_sort(1..1000) },
#    '10000'  => sub { merge_sort(1..10000) },
#    '100000' => sub { merge_sort(1..100000) },
#});

#say(timeit(10, sub { merge_sort(1..1000)  })->real);

sub merge_sort {
    my @items = @_;
    #print "@items\n";
    if (scalar(@items) <= 1) {
        return @items;
    }
    my $half = int(scalar(@items) / 2);
    my @left = merge_sort(@items[0 .. $half-1]);
    my @right = merge_sort(@items[$half .. $#items]);

    my @sorted_items = merge_sorted_arrays(\@left, \@right);
    return @sorted_items;
}

sub merge_sorted_arrays {
    my ($left, $right) = @_;

    my @sorted_items;

    my ($i, $j) = (0, 0);
    while ($i < @$left and $j < @$right) {
        if ($left->[$i] > $right->[$j]) {
            push @sorted_items, $left->[$i];
            $i++;
        } else {
            push @sorted_items, $right->[$j];
            $j++;
        }
    }
    if ($i < @$left) {
        push @sorted_items, @$left[$i .. $#$left];
    } else {
        push @sorted_items, @$right[$j .. $#$right];
    }

    return @sorted_items;
}

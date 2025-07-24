use strict;
use warnings;
use 5.010;

use Benchmark qw(:hireswallclock);
#say(timeit(1, sub { count(1000)  })->real);
#say(timeit(1, sub { count(10000)  })->real);

#timethis(1, sub { count(10000) });   # (warning: too few iterations for a reliable count)
#timethis(100, sub { count(1000) });

timethese(1, {
    '1' => sub { count(1000) },
    '10' => sub { count(10000) },
});


sub count {
    my ($n) = @_;
    for my $i (1 .. $n) {
        for my $j (1 .. $n) {
            my $square = $i+$j;
        }
    }
}



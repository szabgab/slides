use feature 'say';

sub add {
    my ($x, $y) = @_;
    $x + $y
}

say "ok";
my $first = "19";
my $second = 23;
say add($first, $second);

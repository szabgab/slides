sub sum {
    my $sum = 0;
    $sum += $_ for (@_);
    return $sum;
}

sub multiply {
    return 0 if not @_;
    my $res = shift;
    $res *= $_ for (@_);
    return $res;
}

1;


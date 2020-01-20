
$calc_base = 10;

sub calc_add {
    calc_validate_parameters(@_);

    my $total = 0;
    $total += $_ for (@_);
    return $total;
}

sub calc_multiply {
}

sub calc_validate_parameters {
    die 'Not all of them are numbers'
        if  grep {/\D/} @_;
    return 1;
}

1;

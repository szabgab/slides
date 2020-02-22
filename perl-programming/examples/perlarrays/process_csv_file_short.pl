while (<>) {
    $sum += (split /;/)[2];
}
print "$sum\n";


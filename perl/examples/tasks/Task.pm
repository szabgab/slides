package Task;
use strict;
use warnings;

sub count {
    my ($max) = @_;
    my $counter = 0;
    while ($counter < $max) {
        $counter++;
    }
}

sub process_file {
    my ($file) = @_;
    my $total = 0;
    open my $fh, '<', $file or die;
    while (my $line = <$fh>) {
        chomp $line;
        my @fields = split /,/, $line;
        $total += $fields[2];
    }
    return $total;
}


1;

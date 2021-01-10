use strict;
use warnings;

my ($n, $size) = @ARGV;
die "Usage: $0 NUMBER_OF_FILES  SIZE_OF_FILES\n" if not defined $size;

my $content = "";
my $cnt = 0;
while ($cnt < $size) {
    $cnt++;
    $content .= "a,b,$cnt,c,d\n";
}

for my $ix (1..$n) {
    my $filename = sprintf "data_%02s.csv", $ix;
    #print "$filename\n";
    open my $fh, '>', $filename or die "Could not open $filename\n";
        print $fh $content;
        print $fh "a,b,$ix,c,d\n";
}

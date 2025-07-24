use strict;
use warnings;

my $file = 'data.txt';

my @positive;
open my $fh, '<', $file or die "Could not open $file : $!";
while (my $line = <$fh>) {
   if ($line > 0) {
     push @positive, $line;
   }
}
print @positive;


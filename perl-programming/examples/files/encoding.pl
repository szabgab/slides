use strict;
use warnings;

my $file = "data.txt";

open(my $fh, '<:encoding(utf8)', $file) or die "Could not open '$file'\n";
...

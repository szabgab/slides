use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";

use Point;
use Line;

my $point1 = Point->new(x => 10, y => 20);
my $point2 = Point->new(x => 15, y => 25);

my $line = Line->new($point1, $point2);
print $line->isa('Line') ? 'ok' : 'false';
print " - Line\n";

print $line->length, "\n";

use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";

use Point::Small;


my $point = Point::Small->new(x => 10, y => 20);
print $point->isa('Point::Small') ? 'ok' : 'false';
print " isa Point::Small\n";

print $point->isa('Point') ? 'ok' : 'false';
print " isa Point\n";

print $point->get_x, "\n";  # 10
print $point->get_y, "\n";  # 20

$point->show;

#my $point2 = Point::Small->new(x => 150, y => 8);


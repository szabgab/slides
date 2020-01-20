use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";

use Point::3D;


my $point = Point::3D->new(x => 10, y => 20, z => 30);
print $point->isa('Point::3D') ? 'ok' : 'false';
print " isa Point::3D\n";

print $point->isa('Point') ? 'ok' : 'false';
print " isa Point\n";

print $point->get_x, "\n";  # 10
print $point->get_y, "\n";  # 20
print $point->get_z, "\n";  # 30

my $point2 = Point::3D->new(x => 15, y => 25, z => 35);

print $point2->get_x, "\n"; # 15
print $point2->get_y, "\n"; # 25
print $point2->get_z, "\n"; # 35


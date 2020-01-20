use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";

use Point3D;
use Line3D;

my $point1 = Point3D->new(x => 10, y => 20, z => 30);
my $point2 = Point3D->new(x => 15, y => 25, z => 35);

my $line = Line3D->new($point1, $point2);
print $line->isa('Line3D') ? 'ok' : 'false';
print " - Line3D\n";
print $line->isa('Line') ? 'ok' : 'false';
print " - Line\n";

print $line->length, "\n";

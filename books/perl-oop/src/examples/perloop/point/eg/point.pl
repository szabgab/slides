use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";


use Point;

my $p = Point->new();

$p->set_x( 23 );
$p->set_y( 12 );
print $p->get_x, "\n";
print $p->get_y, "\n";

my $q = Point->new(x => 10, y => 20);

print $q->get_x, "\n";
print $q->get_y, "\n";

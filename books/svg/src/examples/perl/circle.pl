use strict;
use warnings;
use SVG (-nocredits => 1, -inline => 1);

my $svg= SVG->new( width => 200, height => 200);
$svg->circle( cx => 100, cy => 100, fill => "#f37", r => 50);
print $svg->xmlify();

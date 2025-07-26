use strict;
use warnings;
use SVG (-nocredits => 1, -inline => 1);

my $svg= SVG->new( width => 200, height => 200);
$svg->rectangle(
    x      => 10,
    y      => 20,
    width  => 180,
    height => 120,
    rx     => 10,
    ry     => 30,
    fill   => "#3a83c5",
);
print $svg->xmlify();

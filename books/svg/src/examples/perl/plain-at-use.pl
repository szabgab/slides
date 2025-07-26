use strict;
use warnings;
use SVG (-nocredits => 1, -inline => 1);

my $svg= SVG->new();
print $svg->xmlify();

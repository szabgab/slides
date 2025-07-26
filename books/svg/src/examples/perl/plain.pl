use strict;
use warnings;
use SVG;

my $svg= SVG->new(-nocredits => 1, -inline => 1);
print $svg->xmlify();

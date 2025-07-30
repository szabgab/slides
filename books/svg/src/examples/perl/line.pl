use strict;
use warnings;
use SVG (-nocredits => 1, -inline => 1);

my $svg= SVG->new( width => 200, height => 200);
$svg->line(
    x1 =>  0,
    y1 =>  0,
    x2 => 200,
    y2 =>  200,
    style => "stroke:blue;stroke-width:5",
);

$svg->line(
    x1 =>  0,
    y1 =>  200,
    x2 => 200,
    y2 =>  0,
    stroke => "red",
    "stroke-width" => 5,
);

# green horizontal line
$svg->line(
    x1 =>  0,
    y1 =>  50,
    x2 =>  200,
    y2 =>  50,
    stroke => "#0F0",
    "stroke-width" => 5,
);


# vertical line
$svg->line(
    x1 =>  50,
    y1 =>  0,
    x2 =>  50,
    y2 =>  200,
    stroke => "rgb(86, 126, 169)",
    "stroke-width" => 5,
);


print $svg->xmlify();


use strict;
use warnings;
use SVG (-nocredits => 1, -inline => 1);

my $IMAGE_WIDTH = 400;
my $IMAGE_HEIGHT = 400;
my $DEFAULT_NUMBER_OF_PIXELS = 20;

die "Usage: $0 WIDTH (in real pixels) HEIGHT (in real pixels) SIZE (how many real pixels is the side of a pixel in the grid)\n"
    if @ARGV != 3;

my ($width, $height, $size) = @ARGV;
my $svg = draw_grid(@ARGV);
draw_diagonal_line($svg, @ARGV);
print $svg->xmlify();

sub draw_diagonal_line {
    my ($svg, $width, $height, $size) = @_;
    for my $box (1..$height/$size) {
        # horizontal line
        $svg->rectangle(
            x =>  ($box-1) * $size,
            y =>  ($box-1) * $size,
            width =>  $size,
            height =>  $size,
            fill => "red",
        );
    }

}


sub draw_grid {
    my ($width, $height, $size) = @_;
    die "Width of $width cannot be divided by $size\n"
        if $width / $size != int($width / $size);
    die "Height of $height cannot be divided by $size\n"
        if $height / $size != int($height / $size);

    my $svg = SVG->new( width => $width, height => $height);

    for my $row (0..$height/$size) {
        # horizontal line
        $svg->line(
            x1 =>  0,
            y1 =>  $row * $size,
            x2 =>  $width,
            y2 =>  $row * $size,
            stroke => "black",
            "stroke-width" => 1,
        );
    }


    for my $column (0..$width/$size) {
        # vertical line
        $svg->line(
            x1 =>  $column * $size,
            y1 =>  0,
            x2 =>  $column * $size,
            y2 =>  $height,
            stroke => "black",
            "stroke-width" => 1,
        );
    }
    return $svg;
}

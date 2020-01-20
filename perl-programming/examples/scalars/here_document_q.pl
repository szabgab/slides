use strict;
use warnings;

my $str = <<'END_STRING';
Some text

$this_is_not_interpolated

more text

END_STRING

print $str;

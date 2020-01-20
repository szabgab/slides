use strict;
use warnings;

use Test::More;
use Test::LongString;

plan tests => 2;

my ($expected, $actual) = generate(200, 170);
is $actual, $expected;

is_string $actual, $expected;




sub generate {
  my ($cnt, $loc) = @_;

  my @chars = ('a' .. 'z', 'A' .. 'Z');
  my $str = '';
  $str .= $chars[ rand scalar @chars ] for 1..$cnt;

  my $actual   = $str;
  substr($actual, $loc, 1, ' ');

  return ($str, $actual);
}



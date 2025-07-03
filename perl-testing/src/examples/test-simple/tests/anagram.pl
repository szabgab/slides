use strict;
use warnings;

use FindBin;
use lib "$FindBin::Bin/../lib";
use MyAnagram qw(is_anagram);

use Test::Simple tests => 5;

ok( is_anagram("abc", "abc") );
ok( is_anagram("silent", "listen") );

ok( not is_anagram("abc", "abd") );

ok( is_anagram("anagram", "nag a gram") );
ok( is_anagram("ABC", "abc") );

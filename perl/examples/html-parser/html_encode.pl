use strict;
use warnings;

use HTML::Entities qw(decode_entities encode_entities);


print decode_entities("x&eacute;x"), "\n";
print decode_entities("x&aring;x"), "\n";
print encode_entities(decode_entities("x&aring;x")), "\n";


print encode_entities('This expression $x < 3'), "\n";
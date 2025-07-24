use strict;
use warnings;

'xaaab' =~ /xa*/;
print "$&\n";

'xabxaab' =~ /xa*/;
print "$&\n";

'xabxaab' =~ /a*/;
print "$&\n";


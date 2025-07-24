use strict;
use warnings;

my ($sig, @process) = @ARGV;

die "Usage: $0 SIGNAL PROCESS-ID\n" if not @process;
kill $sig, @process;


use strict;
use warnings;

use Test::More tests => 1;

use POSIX qw(locale_h);
my $locale = setlocale(LC_CTYPE);
diag $locale;

# OSX/English: en_US.UTF-8
# Windows:
# Hebrew_Israel.1255

my $ipconfig = 'Windows IP Configuration';
if ($locale eq 'German_Germany.1252') {
    $ipconfig = 'Windows-IP-Konfiguration';
}

SKIP: {
    skip "Windows related tests", 1 if $^O !~ /MSWin/i;
    like( `ipconfig`, qr/$ipconfig/ );
}


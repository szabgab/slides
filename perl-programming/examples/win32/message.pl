use 5.010;
use Modern::Perl;

use Win32;


# Win32::MsgBox('hello');

my $resp = Win32::MsgBox('hello', 3, 'Some title');
Win32::MsgBox($resp);

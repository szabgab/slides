use 5.010;
use Modern::Perl;
use Win32::EventLog;

my $h = Win32::EventLog->new('System', $ENV{ComputerName}) or die;
my $recs;
my $base;
$h->GetNumber($recs);
say $recs;

$h->GetOldest($base);
say $base;

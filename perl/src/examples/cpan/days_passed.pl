use strict;
use warnings;


use DateTime;

my $d1 = DateTime->new(year => 2010, month => 8, day => 7, second => 37);
my $d2 = DateTime->new(year => 2010, month => 6, day => 17);

my $sec = $d2->subtract_datetime_absolute($d1)->seconds;
print $sec/60/60/24, "\n";

my $dur = $d1->delta_days($d2);
print $dur->in_units('days'), "\n";



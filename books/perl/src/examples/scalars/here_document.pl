use strict;
use warnings;

my $fname = 'Foo';
my $lname = 'Bar';

my $str = <<"END_REPORT";
Daily user report
------------------

User details:
  Name: $fname $lname

END_REPORT

print $str;

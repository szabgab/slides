use strict;
use warnings;
use 5.010;

use My::EasyApp;

use Log::Log4perl qw(:easy);
Log::Log4perl->easy_init($WARN);
FATAL "This is", " fatal";
ERROR "This is error";
WARN  "This is warn";
INFO  "This is info";
DEBUG "This is debug";
TRACE "This is trace";

my $app = My::EasyApp->new;
$app->run;


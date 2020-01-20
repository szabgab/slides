use strict;
use warnings;
use 5.010;

use Selenium::Remote::Driver;
 
my $driver = Selenium::Remote::Driver->new(
    auto_close => 0,
);
$driver->get('https://duckduckgo.com/');
say $driver->get_title();
#sleep 5;
#$driver->quit();

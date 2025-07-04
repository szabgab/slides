use strict;
use warnings;
use 5.010;

use Selenium::Remote::Driver;
 
my $driver = Selenium::Remote::Driver->new(
    browser_name => 'chrome',
);
$driver->get('https://duckduckgo.com/');
sleep 5;
say $driver->get_title();
$driver->quit();


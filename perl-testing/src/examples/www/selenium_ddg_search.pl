use strict;
use warnings;
use 5.010;

use Selenium::Remote::Driver;
use Selenium::Remote::WDKeys qw(KEYS);
 
my $driver = Selenium::Remote::Driver->new;
$driver->get('https://duckduckgo.com/');
my $input = $driver->find_element('search_form_input_homepage', 'id');
$input->send_keys('perl');
sleep 5;

$input->send_keys(KEYS->{'enter'});
sleep 5;

say $driver->get_title();
$driver->quit();

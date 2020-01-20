use strict;
use warnings;
use 5.010;

use Test::More tests => 4;
use Test::Selenium::Remote::Driver;
use Selenium::Remote::WDKeys qw(KEYS);
 
my $driver = Test::Selenium::Remote::Driver->new;
$driver->get_ok('https://duckduckgo.com/');
$driver->title_is('DuckDuckGo', 'title');
my $input = $driver->find_element('search_form_input_homepage', 'id');
$input->send_keys('perl');
#sleep 5;

$input->send_keys(KEYS->{'enter'});
#sleep 5;

$driver->title_is('perl at DuckDuckGo', 'title');
$driver->body_text_contains('Official Site');
$driver->quit();


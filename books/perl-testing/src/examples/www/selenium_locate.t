use strict;
use warnings;
use 5.010;

use Test::More;
use Test::Selenium::Remote::Driver;
use Selenium::Remote::WDKeys qw(KEYS);

if (not Test::Selenium::Remote::Driver->server_is_running()) {
    plan skip_all => 'The Selenium server must be running for this test';
}

plan tests => 1;

my $url = 'http://localhost:8080/'; 
my $driver = Test::Selenium::Remote::Driver->new;

subtest plain => sub {
    plan tests => 13;
    $driver->get_ok($url);

    my $h1 = $driver->find_element('h1', 'tag_name');
    is $h1->get_text, 'Our languages';

    my $h2;
    eval {
        $h2 = $driver->find_element('h2', 'tag_name');
    };
    ok !$@, 'found h2';

    is $driver->find_element('calculator', 'id')->get_text, 'calculator', 'find by id';

    my $js = $driver->find_element('js', 'class');
    is $js->get_text, 'JavaScript', 'js located';

    my @jses = $driver->find_elements('js', 'class');
    is scalar @jses, 3, 'count of js-es';
    is $jses[0]->get_text, 'JavaScript',        'link 1';
    is $jses[1]->get_text, 'js calculator',     'link 2';
    is $jses[2]->get_text, 'jquery calculator', 'link 3';
 
    #my $link = $driver->find_element('a[class="js"]', 'css');
    my $link = $driver->find_element('a.js', 'css');
    is $link->get_text, 'js calculator';

    my $div = $driver->find_element('//div', 'xpath');
    is $div->get_attribute('id'), 'links', 'links div';


    my $calc_link = $driver->find_child_element($div, 'js calculator', 'link_text');
    is $calc_link->get_attribute('href'), "${url}js_calc.html", 'href'; 


    my $jq_link = $driver->find_child_element($div, 'jquery', 'partial_link_text');
    is $jq_link->get_attribute('href'), "${url}jquery_calc.html", 'href'; 
};


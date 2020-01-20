use Test::More;
use Test::Mojo;

use FindBin;
require "$FindBin::Bin/app.pl";

my $t = Test::Mojo->new;
$t->get_ok('/')
    ->status_is(200)
    ->text_is('head > title' => 'TODO')
    ->element_exists('a[href=/]')
    ->text_is('a[href=/]' => 'home')
    ->element_exists('a[href=/add]')
    ->text_is('a[href=/add]' => 'Add')
    ->element_exists('a[href=/list]')
    ->text_is('a[href=/list]' => 'List')
    ->element_exists_not('table > tr')
;

$t->post_ok('/save' => form => {
        title => 'Some title'
    })
    ->status_is(200)
    ->text_is('head > title' => 'Added')
    ->text_is('h1' => 'Added')
;

done_testing();


use Test::More;
use Test::Mojo;


$ENV{TODODB} = time . '.db';
END {
    unlink $ENV{TODODB};
}

use FindBin;
require "$FindBin::Bin/todo.pl";

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
    #->element_exists('a[href=/xyz]')
;

# Make sure there is nothing in the data
$t->get_ok('/list')
    ->status_is(200)
    ->text_is('head > title' => 'Listing TODO items')
    ->element_exists_not('table > tr')
;

$t->get_ok('/add')
    ->status_is(200)
    ->text_is('head > title' => 'TODO')
    ->element_exists('form[action=/save][method=post]')
    ->element_exists('input[type=text][name=title]')
    ->element_exists('textarea[name=details]')
    ->element_exists('input[type=submit][value=Save]')
;

my @TODO = (
    {
        title => 'Buy milk',
    },
    {
        title => 'Write tests',
    },
);

$t->post_ok('/save' => form => {title => $TODO[0]{title}})
    ->status_is(200)
    ->text_is('head > title' => 'Added')
    ->text_is('h1' => 'Added')
;

$t->get_ok('/list')
    ->status_is(200)
    ->text_is('head > title' => 'Listing TODO items')
    ->element_exists('table > tr')
    ->element_count_is('table > tr', 1, 'one entry')
    ->text_is('table > tr > td > a' => $TODO[0]{title})
;

# Test individual todo page
# edit todo item
# delete todo item


done_testing();

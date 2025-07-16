#!/usr/bin/env perl
use strict;
use warnings;

# trying to create a .mobi file

use EBook::MOBI;
my $book = EBook::MOBI->new();
$book->set_filename('my_ebook.mobi');

$book->set_title   ('Read my Wisdome');
$book->set_author  ('Foo Bar');
$book->set_encoding(':encoding(UTF-8)');
$book->add_mhtml_content(q{
<h1>This is a title</h1>
<p>A paragraph</p>
<p>Another paragraph</p>
<h1>Second Title</h1>
<p>para</p>
});


$book->make();
$book->save();


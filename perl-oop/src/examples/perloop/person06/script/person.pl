use strict;
use warnings;
use v5.10;

use Person;

my $student = Person->new( fname => 'Foo', lname => 'Bar' );
say $student->fname; # Foo
say $student->lname; # Bar

$student->lname('Bar-Yosef');
say $student->lname; # Bar-Yosef

$student->fname('Zorg');
say $student->fname; # Foo   (did not change!)

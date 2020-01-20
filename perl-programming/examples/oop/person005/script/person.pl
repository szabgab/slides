use strict;
use warnings;

use Person;

my $teacher = Person->new;

$teacher->name('Foo');

print $teacher->name, "\n";


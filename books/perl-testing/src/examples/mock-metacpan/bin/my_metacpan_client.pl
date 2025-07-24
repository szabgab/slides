use strict;
use warnings;

use lib 'lib';

use Data::Dumper qw(Dumper);
use MyMetaCPAN ();

my $recent_releases = MyMetaCPAN::get_recent_releases(3);
print Dumper $recent_releases;

my $author_releases = MyMetaCPAN::get_releases_by_author('SZABGAB', 2);
print Dumper $author_releases;

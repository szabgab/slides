use strict;
use warnings;

use MyWebAPI;

my ($url, @names) = @ARGV;
die "Usage: URL 1-or-more-EXPRESSION\n" if not @names;

my $myapi = MyWebAPI->new($url);
my $res = $myapi->count_strings(@names);
for my $name (sort keys %$res) {
    print "$name   $res->{$name}\n";
}

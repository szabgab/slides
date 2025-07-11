package MyWebAPI;
use strict;
use warnings;

use LWP::Simple qw(get);

my $URL = 'http://www.dailymail.co.uk/';

sub new {
    return bless {}, shift;
}

sub count_strings {
    my ($self, @strings) = @_;

    my $content = get $URL;

    my %data;
    foreach my $str (@strings) {
        $data{$str} = () = $content =~ /$str/ig;
    }
    return \%data;
}

1;

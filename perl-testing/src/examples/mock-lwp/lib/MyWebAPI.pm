package MyWebAPI;
use strict;
use warnings;

use LWP::Simple qw(get);

sub new {
    my ($class, $url) = @_;
    my $self = bless {}, $class;
    $self->{url} = $url;
    return $self;
}

sub count_strings {
    my ($self, @strings) = @_;

    my $content = get $self->{url};
    #my $content = LWP::Simple::get $self->{url};

    my %data;
    foreach my $str (@strings) {
        $data{$str} = () = $content =~ /$str/ig;
    }
    return \%data;
}

1;


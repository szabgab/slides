#!/usr/bin/perl
use strict;
use warnings;

my $url = 'http://localhost:5000/';
if (defined $ARGV[0]) {
    $url = $ARGV[0];
}
use LWP::UserAgent;
my $ua = LWP::UserAgent->new;
$ua->agent("Internet Explorer/17.1");
my $req = HTTP::Request->new(GET => $url);

my $res = $ua->request($req);

if ($res->is_success) {
    print $res->content;
} else {
    print $res->status_line, "\n";
}
print "\n";

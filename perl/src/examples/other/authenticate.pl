#!/usr/bin/perl
use strict;
use warnings;

use LWP::UserAgent;

my $ua = LWP::UserAgent->new;
my $req = HTTP::Request->new(GET => 'http://www.perl.org.il/he');
my $res = $ua->request($req);
if ($res->is_success) {
    print $res->content;
} else {
    print "fail\n";
    #my $auth = $res->header('WWW-Authenticate');
    #print "$auth\n";
    print $res->www_authenticate;

    print "--------------\n";
    $req->authorization_basic('gabor', '?');
    my $res2 = $ua->request($req);
    print $res2->content;
}

use strict;
use warnings;

use Test::More;
use LWP::UserAgent;

#plan tests => 3;

my $ua = LWP::UserAgent->new;
$ua->timeout(10);
$ua->agent('Test');

#use HTTP::Request;
#HTTP::Request->new('POST',
use Data::Dumper;
#die Dumper $ua->default_headers;
#my $r = $ua->get('http://act.perl.org.il/ilpw2013/login');

#print $r;
#print $r->header;
#<STDIN>;
#print $r->content;
#print Dumper $response;

#my $r = $ua->post('http://localhost:3000/echo',
#    q => 'xyz',
#);

my $r0 = $ua->get('http://act.perl.org.il/ilpw2013/login');
print $r0->status_line;
print Dumper $r0->cookie_jar;
exit;

__END__
#my $req = HTTP::Request->new(POST => 'http://act.perl.org.il/ilpw2013/LOGIN'
#     'credential_0' => 'szabgab',
#     'credential_1' =>  '',
#);


=pod

my $r = $ua->post('http://act.perl.org.il/ilpw2013/LOGIN',
#     'destination' => '/ilpw2013/',
     'credential_0' => 'szabgab',
     'credential_1' =>  '',
#     'credential_2' =>  '',
#     'join' => 'Submit',
   Referer => 'http://act.perl.org.il/ilpw2013/login',
  );
=cut

if ($r->is_success) {
   print "success\n";
#   print $r->content;
} else {
   print "fail\n";
   print $r->status_line;
#   print $r->content;
}


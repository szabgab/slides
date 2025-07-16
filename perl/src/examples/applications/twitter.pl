#!/usr/bin/env perl

use strict;
use warnings;
use autodie;
use 5.010;

#use Term::ReadPassword::Win32;
use Net::Twitter::Lite;
use Data::Dumper;
#use File::Spec;
#use Cwd;
#print Cwd::abs_path($0);
#print Dumper [ File::Spec->splitpath($0)];
#exit;
my $file = "$0.txt";

die "Put the message in quotes!" if @ARGV > 1;
my $message = $ARGV[0];

print "Welcome to the twitter client.\n";
#print "Please type in your Twitter username: ";
#my $username = <STDIN>;
#chomp $username;
#my $password = read_password("And your password: ");

if (not $message) {
    print "Please type in your message: ";
    $message = <STDIN>;
    chomp $message;
}
my %consumer_tokens = (
    consumer_key    => '',
    consumer_secret => '',
);

my $nt = Net::Twitter::Lite->new(
    %consumer_tokens,
    legacy_lists_api => 0,
);


my @access_tokens;
if (-e $file) {
   open my $fh, '<', $file;
   @access_tokens = <$fh>;
   chomp @access_tokens;
   close $fh;
    $nt->access_token($access_tokens[0]);
    $nt->access_token_secret($access_tokens[1]);
} else {
    my $auth_url = $nt->get_authorization_url;
    say "Visit this URL and authorize the application $auth_url";
    say "Take the PIN code from the response page and type it in";
    my $pin = <STDIN>;
    chomp $pin;
    my @access_tokens = $nt->request_access_token(verifier => $pin);
	open my $out, '>', $file;
    print $out join "\n", @access_tokens;
	close $out;
}

my $result = eval { $nt->update($message) };
print $@;
print "\nResult: $result\n";

#my $status = $nt->user_timeline({ count => 1 });
#print Dumper $status;

__END__



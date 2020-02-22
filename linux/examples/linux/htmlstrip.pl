#!/usr/bin/env perl
use strict;
use warnings;

use Getopt::Long qw(GetOptions);
use HTML::Strip;

GetOptions('help' => \&usage) or usage();

if (@ARGV) {
	foreach my $file (@ARGV) {
		my $content;
		if (open my $fh, '<', $file) {
			local $/ = undef;
			$content = <$fh>;
		} else {
			warn "Could not open '$file'";
			next;
		}
		if ($content) {
			strip($content);
		}
	}
} else {
	my $content = join '', <STDIN>;
	strip($content);
}

sub strip {
	my ($raw_html) = @_;
	my $hs = HTML::Strip->new();
	my $clean_text = $hs->parse( $raw_html );
	$hs->eof;
	print $clean_text;
}

sub usage {
	print <<"USAGE";
Usage:
    $0 filename
    cat file | $0
USAGE
	exit;
}

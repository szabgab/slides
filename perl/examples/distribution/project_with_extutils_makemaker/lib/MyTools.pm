package MyTools;
use strict;
use warnings;
use 5.010;

our $VERSION = '0.01';
use Exporter qw(import);
our @EXPORT_OK = qw(add);

=head1 NAME

MyTools - some tools to show packaging

=head1 SYNOPSIS

Short example

=cut

sub add {
	return $_[0] + $_[1];
}

sub multiply {
	return $_[0] * $_[1];
}


1;


package MyTools;
use strict;
use warnings;
use 5.008;

our $VERSION = '0.01';
use base 'Exporter';
our @EXPORT = qw(add);

=head1 NAME

MyTools - some tools to show in class

=head1 SYNOPSIS

Short example

=cut

sub add {
	return $_[0] + $_[1];
}

1;



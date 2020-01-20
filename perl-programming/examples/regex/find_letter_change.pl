#!/usr/bin/perl
use strict;
use warnings;

#../regex/examples/text/american-english
my $filename = shift or die;

my $data;
{
    open my $fh, '<', $filename or die;
    local $/ = undef;
    $data = <$fh>
}
if ($data =~ /(^a.*\nb.*\n)/mi) {
    print $1;
}



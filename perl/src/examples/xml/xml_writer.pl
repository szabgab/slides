#!/usr/bin/perl
use strict;
use warnings;

use XML::Writer;

open my $out, '>', 'out.xml' or die;

my $writer = XML::Writer->new( OUTPUT => $out, NEWLINES => 0 );

$writer->startTag('data');
$writer->startTag('country', 'id' => 1);
$writer->startTag('name');
$writer->characters('USA');
$writer->endTag('name');
$writer->endTag('country');
$writer->endTag('data');
$writer->end();

close $out;


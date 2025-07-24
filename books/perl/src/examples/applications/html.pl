#!/usr/bin/env perl
use strict;
use warnings;

use CGI;
use HTML::Template;

my $template = HTML::Template->new(filename => "examples/html.tmpl");
my $q = CGI->new;
print $q->header;


if ($q->param("text")) {
    my $text = $q->param("text");
    $template->param(echo => $text);
}
print $template->output


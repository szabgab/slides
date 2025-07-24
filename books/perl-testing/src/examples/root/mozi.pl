use strict;
use warnings;

use WWW::Mechanize::Firefox;

my $m = WWW::Mechanize::Firefox->new;
$m->get('http://google.com/');
#print $m->content;

use Data::Dumper;
#my ($f) = $m->forms;
$m->form_number(1);
my ($f) = $m->current_form;
print $f;
#print Dumper $f;
#print $f->fields;

__END__
print $m->submit_form(
	with_fields => {
	},
);

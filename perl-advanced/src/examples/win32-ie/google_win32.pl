use strict;
use warnings;

use Win32::IE::Mechanize;
my $w = Win32::IE::Mechanize->new(visible => 1);
$w->get("http://www.google.com/ncr");
$w->follow_link(text_regex => qr/advanced/i);

=pod
foreach my $f ($w->forms()) {
    printf("Name: %s\n", $f->name);
    foreach my $in ($f->inputs) {
        printf("   Input: %s %s %s\n",
            $in->name, $in->type, $in->value);
    }
}
=cut

$w->form_name("f");
$w->select("num", 20);
$w->submit_form(
#    form_name => 'f',
    fields => {
        as_q => 'perl training',
    },
);

# But specifically with Google, you should use their API and not their web site

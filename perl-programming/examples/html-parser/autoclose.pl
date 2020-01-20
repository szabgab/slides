use strict;
use warnings;

use HTML::Parser ();

sub event_handler {
    my ($event, $elem) = @_;
    print "$event $elem\n";
}


my $p = HTML::Parser->new(api_version => 3);
$p->handler( start => \&event_handler, "event, tagname");
$p->handler( end   => \&event_handler, "event, tagname");
$p->parse('<head><title>abc</title></head>');
$p->eof;
print "----\n";
$p->parse('<head><title>abc</head>');
$p->eof;

print "----\n";
$p->parse('<ul><li>abc</li><li>def</ul>');
$p->eof;
exit;

use strict;
use warnings;

use HTML::Parser ();

sub start_handler {
    my ($elem, $self) = @_;
#    print "start $elem\n";
    return if $elem ne "title";
    $self->handler(text => sub { print shift }, "dtext");
    $self->handler(end  => sub { shift->eof if shift eq "title"; }, "tagname,self");
}

my $p = HTML::Parser->new(api_version => 3);
$p->handler( start => \&start_handler, "tagname,self");
my $filename = shift || 'title_source.html';
$p->parse_file($filename) or die "Could not parse '$filename' $!";
print "\n";
  

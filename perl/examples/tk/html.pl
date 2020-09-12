use strict;
use warnings;

use Tk;
use Tk::HyperText;

use Browser::Open qw(open_browser open_browser_cmd);


my $top = MainWindow->new;

my $html = $top->HyperText();
$html->pack;
$html->setHandler (Resource => \&onResource);

$html->loadString(qq{<html>
  <head>
  <title>Hello world!</title>
  </head>
  <body bgcolor="#0099FF">
  <font size="6" family="Impact" color="#FFFFFF">
  <strong>Hello, world!</strong>
  </font>
   <h1>Links</h1>
   <ul>
      <li><a href="https://perlmaven.com/">Perlmaven</a></li>
      <li><a href="https://code-maven.com/">Code Maven</a></li>
      <li><a href="https://www.patreon.com/szabgab">Patreon of Gabor</a></li>
   </ul>
  </body>
  </html>
});


MainLoop;

sub onResource {
    my ($html, %info) = @_;
    my $url = $info{href};
    #print $url, "\n";
    #open_browser($url); # https://rt.cpan.org/Public/Bug/Display.html?id=133315
    #print "done\n";
    my $cmd = open_browser_cmd($url);
    # TODO: verify that the URL is well formatted before passing it to system
    if ($^O eq 'MSWin32') {
        system("$cmd $url");
    } else {
        system("$cmd $url &");
    }
}

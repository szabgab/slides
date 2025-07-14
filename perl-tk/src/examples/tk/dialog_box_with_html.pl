use strict;
use warnings;
use 5.010;

use Tk;
use Tk::DialogBox;
use Tk::HyperText;
use Browser::Open qw(open_browser open_browser_cmd);

my $top = MainWindow->new;
my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;
MainLoop;

sub set_color {
    my ($dialog, $color) = @_;
    say $color;
    $btn->configure(-background => $color);
    $dialog->Exit();
}

sub do_on_click {
    my $dialog = $top->DialogBox(
        -title   => 'Versions',
        -popover => $top,
        -buttons => ['OK'],
    );

    my $html = $dialog->HyperText();
    $html->pack;
    $html->setHandler (Resource => \&onResource);
    $html->loadString(q{<html>
      <head>
      <title>Hello world!</title>
      </head>
      <body>
      <h1>Links</h1>
       <ul>
          <li><a href="https://perlmaven.com/">Perlmaven</a></li>
          <li><a href="https://code-maven.com/">Code Maven</a></li>
          <li><a href="https://www.patreon.com/szabgab">Patreon of Gabor</a></li>
       </ul>
      </body>
      </html>
    });

    $dialog->Show;
}

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

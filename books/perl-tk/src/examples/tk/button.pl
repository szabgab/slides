use strict;
use warnings;

use Tk;

sub do_on_click {
    print("Clicked\n");
}


my $top = MainWindow->new;
my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;

MainLoop;

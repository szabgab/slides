use strict;
use warnings;

use Tk;


my $top = MainWindow->new;
my $entry = $top->Entry(
    -font => ['fixed', 40],
);
$entry->pack;

my $secret = $top->Entry(
    -font => ['fixed', 40],
    -show => 0,
);
$secret->pack;


my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;

sub do_on_click {
    print($entry->get, "\n");
    print($secret->get, "\n");
    print("Clicked\n");
}


MainLoop;

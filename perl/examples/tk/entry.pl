use strict;
use warnings;

use Tk;


my $top = MainWindow->new;
my $entry = $top->Entry(
    -font => ['fixed', 20],
);
$entry->pack;

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;

sub do_on_click {
    print($entry->get, "\n");
    print("Clicked\n");
}


MainLoop;

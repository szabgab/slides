use strict;
use warnings;

use Tk;


my $top = MainWindow->new;
my $text = $top->Text(
    -state => 'disabled'
);
$text->pack;

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;

sub do_on_click {
    $text->configure('state', 'normal');
    $text->Insert(scalar(localtime) . "\n");
    $text->configure('state', 'disabled');
}


MainLoop;

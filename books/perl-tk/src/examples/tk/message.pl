use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;
my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;
MainLoop;

sub do_on_click {
    my $msg = $top->Message(-text => 'This is some message');
    $msg->pack(-fill => 'x');
}




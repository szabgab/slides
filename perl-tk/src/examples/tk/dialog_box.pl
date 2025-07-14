use strict;
use warnings;
use 5.010;

use Tk;
use Tk::DialogBox;

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
        -buttons => ['Yes', 'No', 'Cancel', 'Redo'],
    );

    $dialog->add("Label", -background => 'yellow', -text => 'Just some yellow text', -font => ['fixed', 20])->pack();
    my $entry = $dialog->add("Entry", -font => ['fixed', 20],)->pack();
    my $res = $dialog->Show;
    if ($res) {
        say $res;
        say $entry->get;
    }
}



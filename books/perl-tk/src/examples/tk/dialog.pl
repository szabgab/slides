use strict;
use warnings;
use 5.010;

use Tk;
use Tk::Dialog;

my $top = MainWindow->new;
my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;
MainLoop;

sub do_on_click {
    my $dialog = $top->Dialog(
        -title   => 'Versions',
        -popover => $top,
        -text    => "Perl $]",
        -justify => 'left',
        -buttons => ['Yes', 'No', 'Cancel', 'Redo'],
    );
    my $res = $dialog->Show;
    say $res;
}



use strict;
use warnings;

use Tk;

my @planets = qw(Mercury Venus Earth Mars Jupiter Saturn);

my $top = MainWindow->new;

my $listbox = $top->Listbox(
    -selectmode => 'single',
    #-selectmode => 'browse',
    #-selectmode => 'multiple',  # just click and select
    #-selectmode => 'extended',  # Ctrl-click to select more
);
$listbox->pack;
$listbox->delete('0','end');
$listbox->insert('end', @planets);

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&do_on_click,
);
$btn->pack;

MainLoop;

sub do_on_click {
    my $selected = $listbox->curselection;
    if (defined $selected) {
        print("Selection: @$selected\n");
        for my $ix (@$selected) {
            print("$planets[$ix]\n");
        }
    } else {
        print "Nothing is selected\n";
    }
}



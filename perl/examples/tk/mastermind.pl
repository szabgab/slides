use strict;
use warnings;
use 5.010;

use Tk;

my $rows = 1;
my $cols = 4;
my @board;

main();
exit();
# ---------------------------------------------------

sub main {
    my $top = MainWindow->new;

    add_menu($top);
    add_board($top);
    reset_board();

    MainLoop;
}

sub button_click {
    my ($row, $col) = @_;
    say "$row $col";
    $board[$row][$col]->configure(-background => "red");
}


sub reset_board {
    for my $row (0 .. $rows-1) {
        for my $col (0 .. $cols-1) {
            $board[$row][$col]->configure(-background => "grey");
        }
    }
}

sub add_board {
    my ($top) = @_;

    for my $row (0 .. $rows-1) {
        for my $col (0 .. $cols-1) {
            my $btn = $top->Button(
                -text    => '',
                -width => 5,
                -command => sub { button_click($row, $col) },
            );
            $btn->pack(-side => 'left');
            $board[$row][$col] = $btn;
        }
    }
}

sub add_menu {
    my ($top) = @_;

    my $main_menu = $top->Menu();

    my $file_menu = $main_menu->cascade(-label => 'MasterMind');
    $file_menu->command(-label => 'Restart', -command => \&reset_board);
    $file_menu->command(-label => 'Quit', -command => sub { exit });
    $top->configure(-menu => $main_menu);
}



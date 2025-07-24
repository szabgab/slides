use strict;
use warnings;
use 5.010;

use Tk;
use Tk::FileSelect;
use Cwd qw(getcwd);

my $text;

main();
exit;
###########################


sub main {
    my $top = MainWindow->new;
    add_menu($top);

    $text = $top->Text(
        -state => 'normal'
    );
    $text->pack(-fill => 'both', -expand => 1);

    MainLoop;
}

sub do_open {
    my ($top) = @_;

    my $start_dir = getcwd();
    my $file_selector = $top->FileSelect(-directory => $start_dir);
    my $filename = $file_selector->Show;
    if ($filename and -f $filename) {
        if (open my $fh, '<', $filename) {
            local $/ = undef;
            my $content = <$fh>;
            $text->delete("0.0", 'end');
            $text->insert("0.0", $content);
        } else {
            say "TODO: Report error $! for '$filename'";
        }
    }
}

sub do_quit {
    say "TODO check if file is changed or not";
    exit();
}


sub add_menu {
    my ($top) = @_;

    my $main_menu = $top->Menu();

    my $file_menu = $main_menu->cascade(-label => 'File');
    $file_menu->command(-label => 'Open', -command => [\&do_open, $top]);
    $file_menu->command(-label => 'Quit', -command => \&do_quit);

    my $about_menu = $main_menu->cascade(-label => 'Help', -underline => 0);
    $about_menu->command(-label => 'About', -command => \&do_about);

    $top->configure(-menu => $main_menu);
}



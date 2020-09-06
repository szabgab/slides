use strict;
use warnings;

use Tk;

my $top = MainWindow->new;

my $main_menu = $top->Menu();

my $file_menu = $main_menu->cascade(-label => 'File');
$file_menu->command(-label => 'Open', -command => \&do_open);
$file_menu->command(-label => 'Quit', -command => sub { exit });

my $action_menu = $main_menu->cascade(-label => 'Action');
$action_menu->command(-label => 'Run', -command => \&run);

my $about_menu = $main_menu->cascade(-label => 'Help', -underline => 0);
$about_menu->command(-label => 'About', -command => \&about);

$top->configure(-menu => $main_menu);

MainLoop;

sub do_open {
    print("open\n");
}

sub run {
    print("run\n");
}

sub about {
    print("about\n");
}

use strict;
use warnings;

use Tk;

my $top = MainWindow->new;

my $main_menu = $top->Menu();

my $file_menu = $main_menu->cascade(-label => 'File', -underline => 0);
$file_menu->command(-label => 'Open', -underline => 0, -command => \&do_open);
$file_menu->command(-label => 'Quit', -underline => 0, -command => sub { exit });

my $action_menu = $main_menu->cascade(-label => 'Action', -underline => 0);
my $run = $action_menu->command(-label => 'Run', -command => \&run, -state => 'disabled');
$action_menu->separator;
$action_menu->command(-label => 'Enable', -command => \&enable);
$action_menu->command(-label => 'Disable', -command => \&disable);
my $debug = 0;
$action_menu->checkbutton(-label => 'Debug', -variable => \$debug);

my $about_menu = $main_menu->cascade(-label => 'Help', -underline => 0);
$about_menu->command(-label => 'About', -command => \&about);

$top->configure(-menu => $main_menu);

MainLoop;

sub do_open {
    print("open\n");
}

sub run {
    print $debug, "\n";
    print("run\n");
}

sub about {
    print("about\n");
}

sub enable {
    $run->configure(-state => 'normal');
}

sub disable {
    $run->configure(-state => 'disabled');
}

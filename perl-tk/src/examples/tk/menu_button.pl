use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

my $main_menu = $top->Menubutton(-text => "File" );
my $file_menu = $main_menu->Menu(
    -menuitems => [
        [Button => 'Hello', -command => sub { say 'Hello' } ],
        [Button => 'Quit', -command => sub { exit } ],
    ]
);

$main_menu->configure(-menu => $file_menu);
$main_menu->pack();

MainLoop;


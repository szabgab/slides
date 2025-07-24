use strict;
use warnings;
use 5.010;

use Tk;

my $top = MainWindow->new;

my $option_menu_value = 'three';

my $option_menu = $top->Optionmenu(
    -variable => \$option_menu_value,
    -options  => [qw(one two three four)],
    -command  => \&option_menu_changed,
);
$option_menu->pack();

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&click_button,
);
$btn->pack;

MainLoop();

sub option_menu_changed {
    my ($item) = @_;
    say "Option menu set to: $item"
}

sub click_button {
    say $option_menu_value;
}

# [Tk::Optionmenu](https://metacpan.org/pod/Tk::Optionmenu)

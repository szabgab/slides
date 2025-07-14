
use strict;
use warnings;
use 5.010;

use Tk;
use Tk::BrowseEntry;

my $top = MainWindow->new;

my $browse_entry_value = 'three';

my $browse_entry = $top->BrowseEntry(
    -variable => \$browse_entry_value,
    -state => 'readonly',
    -command => \&browse_entry_changed,
    -choices => [qw(one two three four)],
);
$browse_entry->insert('end', qw(five six));

$browse_entry->pack();

my $btn = $top->Button(
    -text    => 'Click me',
    -font    => ['fixed', 20],
    -command => \&click_button,
);
$btn->pack;

MainLoop();

sub browse_entry_changed {
    my ($browse_entry) = @_;
    say "Option menu set to: $browse_entry_value"
}

sub click_button {
    say $browse_entry_value;
}

# [Tk::BrowseEntry](https://metacpan.org/pod/Tk::BrowseEntry)


use Tk;
use Tk::Table;

my $top = MainWindow->new;

my $table  = $top->Table(-columns => 2, -rows => 8, -fixedrows => 1, -scrollbars => 'se');
$table->pack(-expand=> 1, -fill => 'both');

foreach my $col (0..1) {
    foreach $row (0..7) {
        my $btn = $table->Button(
            -text => "Entry $row, $col",
            -command => [\&click, $table , $row ,$col],
        );
        $table->put($row, $col, $btn);
    }
}

MainLoop;

sub click {
    my ($table, $row, $col) = @_;
    my $label = $table->Label(-text => "Pressed $row, $col",-relief => 'sunken');
    my $old = $table->put($row, $col, $label);
    #print "$old\n"
}


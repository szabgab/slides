package App;
use Dancer2;

use FindBin;
use File::Spec;

my $counter_file = File::Spec->catfile($FindBin::Bin, 'count.txt');

get '/' => sub {
    my $counter = 0;
    if (-e $counter_file) {
        if (open(my $fh, '<', $counter_file)) {
            $counter = <$fh>;
        }
    }
    $counter++;
    if (open(my $fh, '>', $counter_file)) {
        print $fh $counter;
    }
    return $counter;
};

App->to_app;

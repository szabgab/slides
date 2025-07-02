package App;
use Dancer2;

use FindBin;
use File::Spec;

my $counter_file = $ENV{COUNTER_FILE} || File::Spec->catfile($FindBin::Bin, 'count.json');

get '/' => sub {
    my $html = '<h1>Counters</h1>';
    my $counter = read_data();
    if (%$counter) {
        $html .= "<ul>\n";
        for my $name (keys %$counter) {
            $html .= "<li>$name: $counter->{$name}</li>\n";
        }
        $html .= "</ul>\n";
    }
    return $html;
};

get '/:name' => sub {
    my $name = route_parameters->get('name');
    my $counter = read_data();

    $counter->{$name}++;
    if (open(my $fh, '>', $counter_file)) {
        print $fh encode_json($counter);
    }
    return $counter->{$name};
};


App->to_app;

sub read_data {
    my $counter = {};
    if (-e $counter_file) {
        if (open(my $fh, '<', $counter_file)) {
            local $/ = undef;
            my $json_str = <$fh>;
            $counter = decode_json($json_str);
        }
    }
    return $counter;
}

package App;
use Dancer2;

get '/' => sub {
    my $config = config();
    my $html = '';
    for my $key (sort keys %$config) {
        $html .= "$key = $config->{$key}<br>\n";
    }
    return $html;
};

App->to_app;

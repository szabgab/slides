package App;
use Dancer2;
use Data::Dumper qw(Dumper);

get '/' => sub {
    my $config = config();
    my $html = '<pre>';
    #$html .= to_json($config, {pretty => 1});
    $html .= to_yaml($config);
    $html .= '</pre>';
    return $html;
};

App->to_app;

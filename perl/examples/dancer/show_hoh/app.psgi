package App;
use Dancer2;

use Text::CSV;

set 'template'     => 'template_toolkit';

get '/' => sub {
    my %planets;

    my $filename = 'planets.csv';
    open my $fh, '<', $filename or die;
    my $csv = Text::CSV->new ({
        binary    => 1,
        auto_diag => 1,
    });
    my $header = $csv->getline($fh);
    $csv->column_names($header);
    while (my $row = $csv->getline_hr($fh)) {
        $row->{Distance} = delete $row->{"Distance (AU)"};
        $planets{ $row->{"Planet name"} } = $row;
    }
    return template 'page', { planets => \%planets };
};

App->to_app;

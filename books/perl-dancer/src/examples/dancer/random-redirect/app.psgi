package App;
use Dancer2;

my @urls = qw(
    https://perlmaven.com/
    https://perl.org/
    https://perl.com/
    https://metacpan.org/
    https://www.perlfoundation.org/
    https://perlmonks.org/
);

get '/' => sub {
    return 'Get random <a href="/red">redirect</a>';
};

get '/red' => sub {
    my $num = int rand scalar @urls;
    #return $urls[$num];
    redirect $urls[$num];
};

App->to_app;

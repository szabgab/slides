use strict;
use warnings;

use Plack::Builder;
use Plack::App::File;
use Plack::App::Proxy;

use Plack::App::Directory;
my $app = Plack::App::Directory->new({ root => '.' })->to_app;

builder {
    mount "/openweathermap" => Plack::App::Proxy->new(remote => "http://api.openweathermap.org/")->to_app;
    mount "/imdb" => Plack::App::Proxy->new(remote => "http://www.imdb.com/")->to_app;
    mount '/' => $app;
};


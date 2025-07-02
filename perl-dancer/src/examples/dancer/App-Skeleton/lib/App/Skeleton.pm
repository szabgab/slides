package App::Skeleton;
use Dancer2;

our $VERSION = '0.1';

get '/' => sub {
    template 'index' => { 'title' => 'App::Skeleton' };
};

true;

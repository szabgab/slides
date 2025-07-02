#!/usr/bin/env perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/../lib";


# use this block if you don't need middleware, and only have a single target Dancer app to run here
use App::Skeleton;

App::Skeleton->to_app;

=begin comment
# use this block if you want to include middleware such as Plack::Middleware::Deflater

use App::Skeleton;
use Plack::Builder;

builder {
    enable 'Deflater';
    App::Skeleton->to_app;
}

=end comment

=cut

=begin comment
# use this block if you want to mount several applications on different path

use App::Skeleton;
use App::Skeleton_admin;

use Plack::Builder;

builder {
    mount '/'      => App::Skeleton->to_app;
    mount '/admin'      => App::Skeleton_admin->to_app;
}

=end comment

=cut


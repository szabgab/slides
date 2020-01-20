#!/usr/bin/perl
use strict;
use warnings;

use Cwd qw(abs_path);
use File::Basename qw(dirname);
use Plack::App::Directory;

my $root = dirname(abs_path($0)) . '/www';
my $app = Plack::App::Directory->new({ root => $root })->to_app;


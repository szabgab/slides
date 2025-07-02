use strict;
use warnings;

use Test::More;
use Plack::Test;
use Plack::Util;
use HTTP::Request::Common;
use File::Temp qw(tempdir);
use Path::Tiny qw(path);

my $source_dir = tempdir( CLEANUP => 1 );
my $upload_dir = tempdir( CLEANUP => 1 );
$ENV{UPLOAD_DIR} = $upload_dir;

my $app = Plack::Util::load_psgi './app.psgi';
my $test = Plack::Test->create($app);

subtest main => sub {
    my $res = $test->request(GET '/');

    is $res->status_line, '200 OK', 'Status';
    is $res->content, '<a href="/upload">Upload</a>', 'Content';
};

subtest empty_upload => sub {
    my $res = $test->request(POST '/upload');
    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'Error', 'Content is error';

};

subtest upload => sub {
    my $filename = path($source_dir, 'abc.txt');
    my $original_content = "First row\nSecond row\n";
    path($filename)->spew($original_content);

    my $res = $test->request(POST '/upload', Content_Type => 'form-data',  Content => [ file  => [$filename, 'new.txt']]);
    is $res->status_line, '200 OK', 'Status';
    is $res->content, 'Uploaded', 'Response Content';
    my $uploaded_file = path($upload_dir)->child('new.txt');
    ok -e $uploaded_file, 'file exists';
    my $uploaded_content = $uploaded_file->slurp;
    is $uploaded_content, $original_content, 'content was uploaded';
};


done_testing();

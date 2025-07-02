package App;
use Dancer2;

get '/' => sub {
    return '<a href="/upload">Upload</a>';
};


get '/upload' => sub {
    return q{
        <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" name="submit" value="Upload">
        </form>
    }
};

post '/upload' => sub {
    my $data = request->upload('file');
    return 'Error' if not defined $data;

    my $dir = $ENV{UPLOAD_DIR} || path(config->{appdir}, 'uploads');
    mkdir $dir if not -e $dir;

    my $path = path($dir, $data->basename);
    if (-e $path) {
        return "'$path' already exists";
    }
    $data->link_to($path);
    return "Uploaded";
};

App->to_app;


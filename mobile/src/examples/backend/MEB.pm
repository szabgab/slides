package MEB;
use Dancer ':syntax';

our $VERSION = '0.1';

get '/' => sub {
  template 'index';
};

get '/echo' => sub {
  return 'Echo GET ' . param('txt') . ' at ' . localtime;
};

get '/echo.json' => sub {
  return to_json {
    'method' => 'GET',
    'txt'    => param('txt'),
    'time'   => scalar localtime,
  };
};

post '/echo.json' => sub {
  return to_json {
    'method' => 'POST',
    'txt'    => param('txt'),
    'time'   => scalar localtime,
  };
};

true;

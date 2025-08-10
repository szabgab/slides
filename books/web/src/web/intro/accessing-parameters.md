# Accessing parameters in Dancer

* param('name');
* params->{name};
* %params = params; $params{name};
* $params = params; $params->{name};


Work both with GET and POST; Mixing values from QUERY_STRING and request body.


* For POST requests also: params('body')
* For GET values see: params('query')
* For route parameters: params('route')


# Building a Single-page application
{id: intro}


## Source Code
{id: source-code}

* [D2-Ajax](https://github.com/szabgab/D2-Ajax)
* [Backend Articles](http://perlmaven.com/dancer)
* [Handlebars Articles](http://code-maven.com/handlebars)
* [AngularJS Articles](http://code-maven.com/angular)



## Technology
{id: technology}

* HTML
* CSS
* JavaScript
* [jQuery](https://jquery.com/)
* [jQuery Tablesorter plugin](http://tablesorter.com/)
* [Handlebars.JS](http://handlebarsjs.com/) a JavaScript templating system
* [Perl Dancer](http://perldancer.org/) for the back-end
* [MongoDB](https://www.mongodb.org/)
* [AngularJS](https://angularjs.org/)



## Setting up Vagrant
{id: setting-up-vagrant}

* Install [Vagrant](https://www.vagrantup.com/)
* Install [VirtualBox](https://www.virtualbox.org/)
* vagrant init szabgab/pde
* Edit Vagrantfile adding the following lines:
* config.vm.network "forwarded_port", guest: 5000, host:5000
* config.vm.network "forwarded_port", guest: 3000, host:3000
* vagrant up  (first time this will download 800Mb file)
* [article](http://perlmaven.com/vagrant-perl-development-environment)
* vagrant ssh
* /vagrant is mapped to your directory on the host
* sudo apt-get install tree



## Install Perl and Dancer2
{id: install-perl-and-dancer2}

* cpanm Dancer2
* cpanm MongoDB



## Install Node.JS
{id: install-nodejs}

* [Download NodeJS](https://nodejs.org/)
* npm install -g bower



## Dancer single file
{id: dancer-single-file}
![](examples/singlefile.pl)

```
$ perl singlefile.pl
>> Dancer2 v0.161000 server 1443 listening on http://0.0.0.0:3000
```

```
$ plackup -r singlefile.pl
Watching ./lib singlefile.pl for file updates.
HTTP::Server::PSGI: Accepting connections at http://0:5000/
```

* -p port  listen on port
* -R dir   watch dir as well



## Create Dancer Skeleton
{id: create-dancer-skeleton}

* Create Skeleton


```
dancer2 -a D2::Ajax
```

Creates directory D2-Ajax



## Dancer Directory layout
{id: dancer-directory-layout}
![](examples/dancer_layout.txt)


## Dancer script and module
{id: dancer-script-and-module}
![](examples/1/D2-Ajax/bin/app.psgi)
![](examples/1/D2-Ajax/lib/D2/Ajax.pm)


## Run Dancer
{id: run-dancer}

* plackup -R lib bin/app.psgi
* http://127.0.0.1:5000/



## Clean-up Dancer Skeleton
{id: clean-up-dancer-skeleton}

* Put "Dancer example" in **views/index.tt**
* empty or remove  **public/css/style.css**
* remove footer from **views/layouts/main.tt**

![](examples/1/D2-Ajax/views/index.tt)
![](examples/1/D2-Ajax/views/layouts/main.tt)


## Run tests
{id: dancer-run-tests}

```
perl Makefile.PL
make
make test
```


## Makefile.PL
{id: makefile-pl}
![](examples/1/D2-Ajax/Makefile.PL)


## Dancer Test scripts
{id: test-scripts}
![](examples/1/D2-Ajax/t/001_base.t)
![](examples/1/D2-Ajax/t/002_index_route.t)



## Dancer Config file
{id: dancer-config-file}
![](examples/1/D2-Ajax/config.yml)


## HTML forms
{id: html-forms}
![](examples/form/views/form.tt)


## Log form parameters
{id: log-form-parameters}
![](examples/form/form.pl)

Run this as **plackup -r form.pl** or as **perl form.pl**.



## Accessing parameters in Dancer
{id: accessing-parameters}

* param('name');
* params->{name};
* %params = params; $params{name};
* $params = params; $params->{name};


Work both with GET and POST; Mixing values from QUERY_STRING and request body.


* For POST requests also: params('body')
* For GET values see: params('query')
* For route parameters: params('route')



## Logging in Dancer
{id: logging-in-dancer}

```
debug "hello";
debug param('name');

use Data::Dumper qw(Dumper);
debug Dumpter scalar params;
```


## Passing values to the template
{id: passing-values-to-the-template}
![](examples/form/template.pl)


## Template::Toolkit
{id: template-toolkit}
![](examples/form/views/demo.tt)



## Exercise: Create reverse echo page
{id: exercise-create-reverse-echo-page}

Create a page that shows a single input box and a button. When the user clicks on the button
the form is submitted and the server sends back the same string and the reversed verson of the same
string.


```
Input: hello

Output: hello olleh
```


## Exercise: Implement a TODO list
{id: exercise-todo-list}

The main form has an input box and a button. When the user types in some text and clicks on the button,
the back-end stores in in a JSON file. (Dancer provides functions <b>to_json</b> and <b>from_json</b>.
We can use <b>Path::Tiny ()</b> and then <b>Path::Tiny::path()</b> with <b>slurp_utf8</b> and <b>spew_utf8</b>
to read a file and to write it out.




When saving the item we need to save the text the user typed in and an id number. (We can use the <b>time</b> function
of <b>Time::HiRes</b>.
On the response page list the items we have in the file.


Next to each item add a button with the word "delete" on it.
When clicking on that button, delete the item from the JSON file on the server
and show the list again.




## First Ajax example
{id: first-ajax-example}

* Ajax - Asynchronous JavaScript and XML
* ... but we usually send JSON


Steps


* Route serving JSON
* (Test this route)
* HTML page with JQuery to send AJAX request and handle response
* Route serving the HTML page with the AJAX request




## Add route returning JSON
{id: add-route-returning-json}

* lib/D2/Ajax.pm


```
get '/' => sub {
    template 'index';
};
```
![](snippets/1/lib/D2/Ajax.pm)

* http://127.0.0.1:5000/api/v1/greeting
* curl http://127.0.0.1:5000/api/v1/greeting


```
{"text":"Hello World"}
```


* curl -I http://127.0.0.1:5000/api/v1/greeting


```
HTTP/1.0 200 OK
Date: Mon, 24 Aug 2015 14:21:11 GMT
Server: HTTP::Server::PSGI
Server: Perl Dancer2 0.161000
Content-Type: application/json
Content-Length: 22
```


## Test route returning JSON
{id: test-route-returning-json}

* t/v1.t

![](snippets/1/t/v1.t)



## Page with AJAX request
{id: page-with-ajax-request}
{i: jQuery.get}
![](snippets/1/views/v1.tt)


## Route serving template with AJAX request
{id: route-serving-template-with-ajax-request}

lib/D2/Ajax.pm


```
get '/v1' => sub {
    return template 'v1';
};
```

Try [v1](http://127.0.0.1:5000/v1)



## Next step: Stand alone client
{id: stand-alone-client}


    Create client code that could be served from another server
    or even just as a file on our local machine.




## Stand-alone AJAX client
{id: stand-alone-ajax-client}

URL includes the hostname

![](snippets/1/client/v1.html)

Try: [v1](file:///Users/gabor/work/D2-Ajax/client/v1.html)



## HTTP Access Control (CORS)
{id: cors-http-access-control}

```
XMLHttpRequest cannot load http://127.0.0.1:5000/api/v1/greeting.
No 'Access-Control-Allow-Origin' header is present on the requested resource.
Origin 'null' is therefore not allowed access.
```

lib/D2/Ajax.pm


```
header 'Access-Control-Allow-Origin' => '*';
```

Let's create v2 of the API

![](snippets/2/lib/D2/Ajax.pm)

Try: [v2](file:///Users/gabor/work/D2-Ajax/client/v2.html)



## Testing the v1 and v2 API calls
{id: testing-v1-and-v2-api-calls}

Copy t/v1.t to t/v2.t  and add two lines testing the Access-Control-Allow-Origin header and the lack of it.


```
subtest v1_greeting => sub {
    my $res  = $test->request( GET '/api/v1/greeting' );
    ...
    is $res->header('Access-Control-Allow-Origin'), undef;
}
```

```
subtest v2_greeting => sub {
    my $res  = $test->request( GET '/api/v2/greeting' );
    ...
    is $res->header('Access-Control-Allow-Origin'), '*';
}
```

```
perl Makefile.PL
make
make test
```


## Proxy
{id: proxy}
![](examples/try/proxy.pl)


## Next step: Create reverse echo
{id: create-reverse-echo}


Send data to server that will echo it back.
After reversing the string.




## Reverse echo with AJAX and Dancer
{id: reverse-echo-with-ajax-and-dancer}

* lib/D2/Ajax.pm

![](snippets/3/lib/D2/Ajax.pm)


## Test reverse echo in Dancer
{id: test-reverse-echo-in-dancer}

* t/v2.t

![](snippets/3/t/v2.t)



## Client side of AJAX string reverse
{id: client-side-of-ajax-reverse}
![](snippets/3/client/v2.html)

Try: [v2](file:///Users/gabor/work/D2-Ajax/client/v2.html)



## Refactoring Dancer app - use the before hook
{id: refactoring-dancer-app-before-hook}

```
header 'Content-Type' => 'application/json';
header 'Access-Control-Allow-Origin' => '*';
```
![](snippets/4/lib/D2/Ajax.pm)


## Silencing the noisy tests
{id: silencing-the-noisy-test}

```
make test
```
![](snippets/noisy_test_output.txt)

```
BEGIN {
    $ENV{DANCER_ENVIRONMENT} = 'test';
}
```
![](snippets/test_output.txt)


## Next step: TODO list
{id: create-todo-list}

* Back-end: Save item in the back-end in MongoDB
* Form that accepts text sends to the server
* Back-end: Fetch list of all item
* List items received from the back-end
* Delete item



## Add item to MongoDB (POST route)
{id: add-item-to-mongodb-post-route}
![](snippets/5/lib/D2/Ajax.pm)


## Test adding item to MongoDB (POST route)
{id: test-add-item-to-mongodb-post-route}
![](snippets/5/t/v2.t)


## MongoDB client
{id: mongodb-client}

```
$ mongo
(mongod-3.0.1) test> use d2-ajax
switched to db d2-ajax
(mongod-3.0.1) d2-ajax> db.items.find()
{
  "_id": ObjectId("55671d33a11460085a6cd701"),
  "text": "First Thing to do"
}
Fetched 1 record(s) in 2ms
```


## Use separate database for testing
{id: separate-database-for-testing}

config.yml


```
app:
  mongodb: d2-ajax
```

lib/D2/Ajax.pm


```
my $db   = $client->get_database( config->{app}{mongodb} );
```

t/v2.t


```
my $db_name = 'd2-ajax-' . $$ . '-' . time;
diag $db_name;
D2::Ajax->config->{app}{mongodb} = $db_name;
```

Drop the database automatically


```
use MongoDB ();
```

```
my $client = MongoDB::MongoClient->new(host => 'localhost', port => 27017);
my $db   = $client->get_database( $db_name );
$db->drop;
```



## Fetch all the items
{id: fetch-all-the-items}

```
use JSON::MaybeXS;
```
![](snippets/6/lib/D2/Ajax.pm)


## Test: Fetch all the items
{id: fetch-all-the-items-test}
![](snippets/6/t/v2.t)


## Add more tests
{id: add-more-tests}
![](snippets/6/t/post_empty_items.t)
![](snippets/6/t/fetch_all_items_again.t)
![](snippets/6/t/post_item_with_spaces.t)



## Add and retrieve elements using jQuery and AJAX
{id: add-and-retrieve-elements-jquery-ajax}
![](snippets/6/client/item_input_form.html)

```
$(document).ready(function() {
    ...
    show_items();
    ...
})
```
![](snippets/6/client/show_items_with_javascript.js)

Data structure in Perl


```
{
  'items' => [
    {
      '_id' => {
        '$oid' => '556d6735a11460452f6e7601'
      },
      'text' => 'First Thing to do'
    },
    {
      '_id' => {
        '$oid' => '556d6735a11460452f6e7602'
      },
      'text' => 'one more'
    }
  ]
}
```


## Add item
{id: add-item}
![](snippets/6/client/add_item.js)


## Setting up Travis-CI
{id: setting-up-travis-ci}
![](snippets/travis.yml)



## Code refactoring: _mongodb
{id: code-refactoring-mongodb}
![](snippets/7/lib/D2/Ajax.pm)

```
my $items = _mongodb('items');
```


## Deleting item: Dancer, MongoDB backend
{id: deleting-item-dancer-mongodb-backend}
![](snippets/8/lib/D2/Ajax.pm)


## Test Deleting item backend
{id: deleting-item-dancer-mongodb-backend-test}
![](snippets/8/t/v2.t)



## Deleting item: client side
{id: deleting-item-client-side}
![](snippets/8/client/show_items.js)

Add click-event handler to every element with "delete" class.


```
$(".delete").click(delete_item);
```
![](snippets/8/client/deleting_item.js)


## Access-Control-Allow-Methods
{id: access-control-allow-methods}

Look at the JavaScript console.


```
XMLHttpRequest cannot load http://127.0.0.1:5000/api/v2/item/556db39fa114604bac0757d1.
No 'Access-Control-Allow-Origin' header is present on the requested resource.
Origin 'null' is therefore not allowed access. The response had HTTP status code 404.
```

```
OPTIONS http://127.0.0.1:5000/api/v2/item/556db39fa114604bac0757d1
```

The command-line console of Dancer.


```
looking for options /api/v2/item/556db39fa114604bac0757d1
```


## Add header: Access-Control-Allow-Methods
{id: header-access-control-allow-methods}

Add to the before hook of lib/D2/Ajax.pm:


```
header 'Access-Control-Allow-Methods' => 'GET, POST, OPTIONS, DELETE';
```

Add to lib/D2/Ajax.pm


```
options '/api/v2/item/:id' => sub {
    return '';
};
```

Test it:

![](snippets/8/t/options.t)


## Replace manual HTML generation by the use of Handlebars
{id: replace-manual-html-generation-with-handlebars}
![](snippets/9/client/old_v2.html)
![](snippets/9/client/v2.html)


## Handlebars code
{id: handlebars-code}
![](snippets/9/client/handlebars.html)
![](snippets/9/client/handlebars.js)


## Add timestamp to item (back-end)
{id: add-timestamp-to-item-back-end}

```
use DateTime::Tiny;
```

```
date => DateTime::Tiny->now,
```
![](snippets/10/lib/D2/Ajax.pm)

mongo client


```
$ mongo
test> use d2-ajax
d2-ajax> db.items.find()
{
  "_id": ObjectId("557593b5a114607aa9188b91"),
  "date": ISODate("2015-06-08T16:08:05Z"),
  "text": "new item"
}
Fetched 1 record(s) in 3ms
```


## Add timestamp to item (back-end TO_JSON)
{id: add-timestamp-to-item-back-end-to-json}

```
Route exception: encountered object '2015-06-08T16:08:05',
but neither allow_blessed, convert_blessed nor allow_tags settings are enabled
(or TO_JSON/FREEZE method missing
```

Run the tests

![](snippets/10/test_output.txt)
![](snippets/10/prove.txt)

Tell MongoDB to use DateTime::Tiny


```
$client->dt_type( 'DateTime::Tiny' );
```
![](snippets/10/prove2.txt)


## Monkey patching DateTime::Tiny
{id: monkey-patching-datetime-tiny}

```
sub DateTime::Tiny::TO_JSON { shift->as_string };
```
![](snippets/10/prove_monkey.txt)

Testing


```
like $items1->{items}[0]{date}, qr/^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d$/;
```


## Add timestamp to item (front-end)
{id: add-timestamp-to-item}
![](snippets/10/client/v2.html)


## jQuery Tablesorter
{id: jquery-tablesorter}

* [tablesorter](http://tablesorter.com/)
* [GitHub](https://github.com/christianbach/tablesorter)

![](snippets/11/client/v2.html)
![](snippets/11/client/include_tablesorter.html)
![](snippets/11/client/tablesorter.html)
![](snippets/11/client/tablesorter.js)


## Add Tablesorter themes
{id: add-tablesorter-themes}


Copy from [GitHub](https://github.com/christianbach/tablesorter)


![](snippets/11/client/tablesorter_themes.html)


## Add Tablesorter Date column
{id: tablesorter-date-column}

Add to the template:


```
class="date" sort="{{ date }}"
```
![](snippets/11/client/tablesorter_date.js)






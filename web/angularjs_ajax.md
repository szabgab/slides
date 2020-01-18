# AngularJS - Ajax - Building a Single Page Application
{id: angularjs-ajax}

## What are Single-page web applications?
{id: what-are-single-page-web-applications}

* Gmail?
* Smooth, no page reload
* "Live" - updates even without interaction
* Back/Forward buttons work properly
* History is being recorded
* [Example](http://127.0.0.1:5000/examples/d2/angular_v2.html)



## Access data on server
{id: access-data-on-server}
{i: $http}
{i: $resource}
{i: ngResource}
{i: Restangular}

* [$http - built in](https://docs.angularjs.org/api/ng/service/$http)
* [$resource [ngResource]](https://docs.angularjs.org/api/ngResource)
* [Restangular](https://github.com/mgonto/restangular)



## Mojolicious Backend
{id: mojolicous-backend}

[back-end](http://127.0.0.1:3000/)


```
$ cd examples/mojo_ajax
$ morbo app.pl
```
![](examples/mojo_ajax/app.pl)



## $http GET request
{id: http-get-request-v1}
{i: $http}
{i: GET}
{i: CORS}
{i: Access-Control-Allow-Origin}
![](examples/d2/angular_v1_greeting.html)
![](examples/d2/angular_v1_greeting.js)

CORS - Cross-Origin Resource Sharing



## $http GET request with CORS enabled
{id: http-get-request-with-cors-enabled-v2}
{i: Access-Control-Allow-Origin}
![](examples/d2/angular_v2_greeting.html)
![](examples/d2/angular_v2_greeting.js)


## $http GET request with data
{id: http-get-request-with-data-v2}
{i: GET}
{i: encodeURIComponent}
![](examples/d2/angular_v2_reverse.html)
![](examples/d2/angular_v2_reverse.js)


## $http POST, OPTIONS requests
{id: http-post-request-v2}
{i: POST}
{i: OPTIONS}

remove examples/mojo_ajax/items.db


```
$ sqlite3 examples/mojo_ajax/items.db
```
![](examples/d2/angular_v2_add_item.html)
![](examples/d2/angular_v2_add_item.js)



## $http list items
{id: http-v2-list-items}
![](examples/d2/angular_v2_list_items.html)
![](examples/d2/angular_v2_list_items.js)


## $http DELETE request
{id: http-v2}
{i: DEL}
![](examples/d2/angular_v2.html)
![](examples/d2/angular_v2.js)



## Using ngResource
{id: resource-get}
{i: ngResource}


<a href="https://docs.angularjs.org/api/ngResource">ngResource</a>


![](examples/angular/resource_v2_get.html)
![](examples/angular/resource_v2_get.js)



## ngResource error handling (no CORS)
{id: resource-get-error}
![](examples/angular/resource_v1_get.html)
![](examples/angular/resource_v1_get.js)


## ngResource GET with param
{id: resource-get-with-data}
![](examples/angular/resource_v2_reverse.html)
![](examples/angular/resource_v2_reverse.js)


## Public APIs with Cross-origin Resource Sharing (CORS) enabled
{id: public-apis}

* [MetaCPAN](https://github.com/CPAN-API/cpan-api/blob/master/docs/API-docs.md)
* [GitHub](https://api.github.com)
* [Google API](https://developers.google.com/api-client-library/javascript/features/cors)
* [Open Weather Map](http://openweathermap.org/)

![](examples/try/cors.html)
![](examples/try/cors.js)
![](examples/try/cors.css)


## MetaCPAN API
{id: metacpan-api}


New API


* [MetaCPAN](https://metacpan.org/)
* <a href="https://api-v1.metacpan.org/release/ETHER/Moose-2.1603"></a>
* [100 most recent](https://api-v1.metacpan.org/release/_search?q=status:latest&amp;fields=name,status,date&amp;sort=date:desc&amp;size=100)
* api-v1 instead of api  and remove the v0/ from the path



Old API


* [100 most recent uploads](http://api.metacpan.org/v0/release/_search?q=status:latest&amp;fields=name,status,date&amp;sort=date:desc&amp;size=100)
* [Authors (limit 3)](http://api.metacpan.org/v0/author/_search?size=3)
* [Authors (show only 2 fields)](http://api.metacpan.org/v0/author/_search?size=3&amp;fields=pauseid,region)
* [Authors (show only PAUSEIDs with sz in them)](http://api.metacpan.org/v0/author/_search?size=3&amp;fields=pauseid,region&amp;q=sz)
* [Distributions](http://api.metacpan.org/v0/distribution/_search?size=3)
* [Distributions (name staring with DBIx)](http://api.metacpan.org/v0/distribution/_search?size=3&amp;q=DBIx)
* [Releases](http://api.metacpan.org/v0/release/_search?size=3)
* [Releases (show only specific fields and only for 'latest' releases](http://api.metacpan.org/v0/release/_search?size=3&amp;fields=author,distribution,status&amp;q=status:latest)
* [Releases (latest, authored by DAVID](http://api.metacpan.org/v0/release/_search?size=3&amp;fields=author,distribution,status&amp;q=status:latest%20AND%20author:DAVID)
* [Modules](http://api.metacpan.org/v0/module/_search?size=3)
* [Modules (called CGI)](http://api.metacpan.org/v0/module/_search?size=3&amp;q=name:CGI)
* [Modules (called CGI* , status:latest, list name and distribution)](http://api.metacpan.org/v0/module/_search?size=3&amp;q=name:CGI*%20AND%20status:latest&amp;fields=name,distribution)



## Exercise: Implement a new interface for MetaCPAN
{id: exercise-ajax}

* [one example](http://cpan.perlmaven.com/)
* [source](https://github.com/szabgab/metacpanjs) with some queries.
* Recent module listing
* Allow the user to select the number of items to be listed.
* Remember the selection between reloads.
* Page to see the documentation of a module
* Remember the modules the user has visited and allow the user to see the history
* ...






# Client
{id: mojolicious-client}

## Mojo::UserAgent
{id: mojolicious-useragent}
{i: Mojo::UserAgent}
{i: Mojo::Message::Response}
{i: res}
{i: body}
![](examples/ua/get_yapcna.pl)

* [Mojo::Message::Response](http://mojolicious.org/perldoc/Mojo/Message/Response)
* [Mojo::UserAgent](http://mojolicious.org/perldoc/Mojo/UserAgent)



## CSS Selectors
{id: mojolicious-ua-find}
{i: dom}
{i: find}
{i: Mojo::DOM}
{i: Mojo::Collection}
![](examples/ua/get_yapcna_select_h1.pl)

* dom returns a [Mojo::DOM](http://mojolicious.org/perldoc/Mojo/DOM)
* find returns a [Mojo::Collection](http://mojolicious.org/perldoc/Mojo/Collection)



## Mojo::UserAgent and JSON
{id: mojolicious-ua-json}
{i: json}
![](examples/ua/metacpan_api_recent_json.pl)


## Mojo::UserAgent and JSON details
{id: mojolicious-ua-json-details}
![](examples/ua/metacpan_api_most_recent.pl)


## Mojo::UserAgent and JSON Pointers
{id: mojolicious-ua-json-pointer}
{i: Mojo::JSON::Pointer}
![](examples/ua/metacpan_api_most_recent_pointer.pl)

* [Mojo::JSON::Pointer](http://mojolicious.org/perldoc/Mojo/JSON/Pointer)



## Easy Debugging
{id: mojo-useragent-debugging}
{i: MOJO_USERAGENT_DEBUG}

```
MOJO_USERAGENT_DEBUG=1 perl application.pl
```


## Mojo::UserAgent on the command line
{id: mojo-ui-command-line}

```
$ mojo get www.yapcna.org/yn2016/ 'title'
```






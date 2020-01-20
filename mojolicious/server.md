# Application
{id: mojolicious-server}

## Hello World
{id: lite-hello-world}
{i: get}
{i: start}
{i: render}
![](examples/lite/hello_world.pl)

**morbo hello_world.pl**


* Visit http://127.0.0.1:3000/
* Look at the console
* Visit http://127.0.0.1:3000/other  to see the error
* Look at the console



## use strict use warnings
{id: lite-use-strict-use-warnings}

* use strict;
* use warnings;
* use utf8;
* use 5.010;



## Your secret passphrase needs to be changed
{id: secret-passphrase}
{i: secrets}
![](examples/lite/hello_world_with_secret.pl)


## Echo form
{id: lite-echo-form}
![](examples/lite/echo_form.pl)

* Visit http://127.0.0.1:3000/echo
* Fill the form and submit




## Echo
{id: lite-echo}
{i: post}
{i: param}
{i: $c}
{i: Mojolicious::Controller}
![](examples/lite/echo.pl)

* [Mojolicious::Controller](http://mojolicious.org/perldoc/Mojolicious/Controller)



## Embedded templates
{id: echo-with-template}
{i: sub}
{i: render}
{i: __DATA__}
![](examples/lite/echo_with_template.pl)


## Embedded templates
{id: echo-with-embedded-templates}
{i: &lt;%=}
{i: %&gt;}
![](examples/lite/echo_with_embedded_templates.pl)


## Merged templates
{id: echo-with-merged-templates}
![](examples/lite/echo_with_merged_templates.pl)


## Conditionals in templates
{id: conditionals-in-templates}
{i: if}
{i: %}
![](examples/lite/conditionals_in_templates.pl)

* Had to add undef to the first call as well.



## Common layout
{id: common-layout}
{i: layout}
![](examples/lite/common_layout.pl)


## Embedded Stylesheet
{id: embedded-stylesheet}
{i: style}
![](examples/lite/embedded_stylesheet.pl)


## External Stylesheet - static files in the 'public' directory
{id: external-stylesheet}
{i: public}
![](examples/lite/1/app.pl)
![](examples/lite/1/public/style.css)


## Generate Mojolicious::Lite skeleton
{id: generate-lite-app-skeleton}
{i: mojo}

* $ mojo generate lite_app myapp.pl
* Warning: will overwrite your existing file without asking questions

![](examples/lite/myapp.pl)

* Visit http://127.0.0.1:3000/  and click on the Perldoc link



## Generate Mojolicious skeleton
{id: generate-mojolicious-skeleton}
{i: mojo}

* $ mojo generate app
* Will generate subdirectory 'my_app' with module name MyApp in my_app/lib/MyApp.pm


```
$ tree my_app/

my_app/
    lib/
        MyApp/
            Controller/
                Example.pm
        MyApp.pm
    public/
        index.html
    script/
        my_app
    t/
        basic.t
    templates/
        example/
            welcome.html.ep
        layouts/
            default.html.ep
```

* $ mojo generate app My::Example
* Will generate subdirectory 'my_example' with module name My::Example in my_example/lib/My/Example.pm



## Mojolicious Routing
{id: mojolicous-routing}


* **get '/list/home'** a route with an exact match
* **get '/item/:id'** a route with a placeholder  won't match . or /
* **get '/phone/#number'**   also accepts .  as in /phone/1.234.567890
* **get '/path/*anything'**  also accepts /


```
$c->param('id');
$c->param('number');
$c->param('anything');
```


## GET routes
{id: get-routes}
![](examples/lite/get.pl)



## EP (Embedded Perl) Templates
{id: ep-templates}
![](examples/lite/embedded_templates.pl)


## EP (Embedded Perl) Templates (HTML)
{id: ep-templates-html}
![](examples/lite/embedded_templates_html.pl)


## Return JSON
{id: return-json}
![](examples/lite/json.pl)


## Testing
{id: testing}
![](examples/lite/test.t)


## Deployment
{id: deployment}

[Mojolicious::Guides::Cookbook](http://mojolicious.org/perldoc/Mojolicious/Guides/Cookbook)


* Apache/CGI
* PSGI/Plack - any such server (without the real-time features of Mojo)




* (Built in) Daemon
* Morbo      (Automatically reloads the server)
* [Hypnotoad](http://mojolicious.org/perldoc/Mojo/Server/Hypnotoad)  Hot-code reloading production server
* Hot deployment: Zero downtime software upgrades



```
hypnotoad project      (start or reload)
hypnotoad -s project   (stop)
```






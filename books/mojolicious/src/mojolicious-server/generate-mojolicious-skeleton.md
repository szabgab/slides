# Generate Mojolicious skeleton

* mojo

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


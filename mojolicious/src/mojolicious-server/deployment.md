# Deployment


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


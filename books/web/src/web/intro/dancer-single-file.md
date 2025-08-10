# Dancer single file

{% embed include file="src/examples/singlefile.pl" %}

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




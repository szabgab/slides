# Mojolicious Routing

* **get '/list/home'** a route with an exact match
* **get '/item/:id'** a route with a placeholder  won't match . or /
* **get '/phone/#number'**   also accepts .  as in /phone/1.234.567890
* **get '/path/*anything'**  also accepts /


```
$c->param('id');
$c->param('number');
$c->param('anything');
```




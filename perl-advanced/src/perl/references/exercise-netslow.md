# Exercise: Create a cache for NetSlow


```
You are using a module call NetSlow.pm and its sole function compute();
This function can get two numbers and after a remote procedure call
(that takes a lot of time) returns a single value. Create a local cache
of the given input values and results so you won't need to access the
remote machine for identical calls. (Make sure your cache is persistent
between execution of your script.

examples/references/NetSlow.pm

Here is how we can use the module: 
```
{% embed include file="src/examples/references/netslow.pl" %}


```
Later on you find out that the results are changing over time.
You don't want to drop the caching and you decide you can live with
certain lack of accuracy. You decide you fetch the value again if 
the last call to that specific set of input values was computed more 
than 5 seconds ago. That is you expire the cache after 5 seconds.
```



# MCE - map running in parallel

* MCE
* fork
* map

* [MCE::Map](https://metacpan.org/pod/MCE::Map)


The MCE package provides a map-like function that automatically runs the different tasks in separate processes then
collects the results in the correct order.

By default it creates 4 child processes, but you can control that and a few other things by calling the init method.


{% embed include file="src/examples/forks/use_mce_map.pl" %}
{% embed include file="src/examples/forks/use_mce_map.out" %}



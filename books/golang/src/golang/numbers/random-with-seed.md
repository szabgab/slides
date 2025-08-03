# Random with seed

* Seed
* time.Now().Unix

* In order to generate different random numbers one needs to set the starting point by calling `Seed`.
* A common way to do that is to provide the number of seconds since the epoch.

{% embed include file="src/examples/random-with-seed/random_with_seed.go" %}
{% embed include file="src/examples/random-with-seed/random_with_seed.out" %}




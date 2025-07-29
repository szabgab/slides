# LRU - Least recently used cache

* [LRU - Cache replacement policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)
* When we call the function with (1, 5) it removes the least recently used results of (1, 2)
* So next time it has to be computed again.

{% embed include file="src/examples/decorators/lru_cache_example_1.py" %}


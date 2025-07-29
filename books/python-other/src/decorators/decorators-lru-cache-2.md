# LRU - Least recently used cache

* Here we called (1, 2) after (1, 4) when it was still in the cache
* When we called (1, 5) it removed the LRU pair, but it was NOT the (1, 2) pair
* So it was in the cache even after the (1, 5) call.

{% embed include file="src/examples/decorators/lru_cache_example_2.py" %}



# Multiprocess: Pool

* multiprocess
* Pool
* map

`Pool(3)` creates 3 child-processes and let's them compute the values. `map`
returns the results in the same order as the input came in.

{% embed include file="src/examples/multiprocess/multiprocess_pool.py" %}

```
python multiprocess_pool.py  11 3
python multiprocess_pool.py  100 5
```



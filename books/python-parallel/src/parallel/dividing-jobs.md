# Dividing jobs

* N items to process
* K in parallel

* Divide the items in K groups of size int(N/K) and int(N/K)+1.
* Create K parallels with one item each. When it is done, give it another item.
* Create K parallels with one item each. When done let it stop and create a new parallel.



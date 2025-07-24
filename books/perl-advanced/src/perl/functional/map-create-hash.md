# Create a hash from an array using map

* map

* We have a list of values. We would like to build a fast look-up table to check for existence.


The time it takes to check if a value can be found in an array is proportional to the length of the array. The complexity is O(n).

If you need to do it a lot of times you might be better off building a hash where the keys are  the items coming from the array. The values
don't matter as we will check the existance of a key. (Alternatively you can set the values of the hash to be 1 and then you can check if the
the value is there.) The time it takes to look up a key in a hash does not depend on the size of the hash. It is O(1). So once we have the hash
the look-up will be much faster. Building the hash is proportional to the number of items in the array.

So if we need to look up a very small number of elements or if the original array is small then probably it is better to just use the array.

If we need a lot of look-ups and there are many elements in the original array then building a temporary look-up hash might be a good idea.

We use more memory but we can gain speed.


{% embed include file="src/examples/functional/map_create_hash.pl" %}



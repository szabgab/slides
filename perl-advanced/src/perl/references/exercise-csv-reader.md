# Exercise: improve the csv reader


```
Instead of an array create a hash in which the key is
the fname and the value is the hash reference.

To get the phone of 'Foo' we could write:

$data{Foo}{phone}
```

* First you can assume fname values are unique.
* Then improve it by checking if the fname is indeed unique and warn if not.
* Further improve it by removing the fname from the internal hashes.
* Further improve by passing the name of the key field (currently fname) as a parameter.
* Bonus: try to deal with the case when there are duplicate values for the key field without just giving an error message.




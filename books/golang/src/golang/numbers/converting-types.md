# Converting values to other types - float32, int, string

* float32()
* int()
* string()
* Sprintf
* %f
* %d

* integers to `float32()`
* floats to `int()`
* integers to `string()` but that converts the number to the value it represents in ASCII or Unicode table.
* In order to get the same "look" but as a string we need to use the `Sprintf` function from `fmt`.


{% embed include file="src/examples/convert/convert.go" %}



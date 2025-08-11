# STDIN don't accept nil

* `gets` will retun `nil` if we press Ctrl-D
* `gets.not_nil!` will raise an exception

{% embed include file="src/examples/other/gets_not_nil.cr" %}



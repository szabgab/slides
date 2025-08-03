# Hello Foo - Println

* Println
* :=


In go you can use the `:=` operator to declare a variable and assign a value to it at the same time. Then you can use that variable in a `Println`.
As you might notice, (I did not when I first tried this), the ``Println` function inserts a space between the values it prints. For better control about this you can use `Printf`.


{% embed include file="src/examples/hello-foo/hello_foo.go" %}
{% embed include file="src/examples/hello-foo/hello_foo.out" %}



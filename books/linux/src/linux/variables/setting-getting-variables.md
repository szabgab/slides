# Setting and getting variables

* $

* Assignment using = without spaces on either side of =
* All the variables are strings. If there are spaces in the value, the whole value mus be in quotes
* When using a variable we must prefix it with a $ sign

{% embed include file="src/examples/script/variables.sh" %}

```
$ ./examples/script/variables.sh
foobar
./examples/script/variables.sh: line 5: programmer: command not found

Hello foobar

foobarit
```


There are empty lines printing the content of 'occupation' and that of the variable 'nameit'.




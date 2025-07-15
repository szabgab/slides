# AUTOLOAD

* AUTOLOAD
* $AUTOLOAD


{% embed include file="src/examples/advanced-perl/no_autoload.pl" %}

```
Output:

Undefined subroutine &main::f called
```



If you call a function that does not exist when the call is made, Perl will raise an `Undefined subroutine called` exception. If the exception is
not handled it will stop your program.

In the exception it will also give you the full name of the function that was missing. In the above case it will be `&main::f`.

With all the other magic, Perl also provides you a tool that will help you deal with such situations. You can include a block called AUTOLOAD
in your code and if AUTOLOAD {} is defined then it will be executed instead of every missing function. From that point your imagination is the
only limiting factor on how to handle the situation.


{% embed include file="src/examples/advanced-perl/autoload.pl" %}

Output:

{% embed include file="src/examples/advanced-perl/autoload.out" %}



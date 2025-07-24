# Modules

We could have placed the package keyword and the code in the main script
or we can put several packages in the same external file but the
best approach is to put every package in a separate file having
the same name as the package itself (case sensitive)
and .pm as file extension.

Then we call it a Perl Module.

{% embed include file="src/examples/modules/module.pl" %}
{% embed include file="src/examples/modules/Calc.pm" %}

* How did perl find the file Calc.pm ?
* How could we use add() without the Calc:: ?
* Why did we write "require" instead of "use"?




# scope

{% embed include file="src/examples/other/scope_before_def.py" %}
{% embed include file="src/examples/other/scope_after_def.py" %}

If we declare a variable outside of all the subroutines,
it does not matter if we do it before the sub declaration,
or after it. In neither case has the global variable any presence
inside the sub.

{% embed include file="src/examples/other/scope_inside_def.py" %}



A name declared inside a subroutine is not visible outside.

{% embed include file="src/examples/other/scope_global.py" %}

Unless it was marked using the global word.


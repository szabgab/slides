# Export import


* __all__
* import
* from

* from mod import a,b,_c  - import 'a', 'b', and '_c' from 'mod'
* from mod import *  - import every name listed in __all__ of 'mod' if __all__ is available.
* from mod import *  - import every name that does NOT start with _ (if __all__ is not available)
* import mod - import 'mod' and make every name in 'mod' accessible as 'mod.a', and 'mod._c'

{% embed include file="src/examples/modules/my_module.py" %}
{% embed include file="src/examples/modules/x.py" %}
{% embed include file="src/examples/modules/y.py" %}




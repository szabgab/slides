# PyTest: Force default order

If for some reason we would like to make sure the order remains the same,
in a given module, we can add the following two lines of code.


```
import pytest
pytestmark = pytest.mark.random_order(disabled=True)
```
{% embed include file="src/examples/pytest/order/test_default_order.py" %}




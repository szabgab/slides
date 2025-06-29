# Do not import *


* Despite the examples you can use in various places, I'd recommend never to import "everything" using `*`.

```
from one import *
from two import *


run()
```

* Where does `run()` come from?
* What if both moduldes have the `run()` function? Then the order of the import will be important.
* What if the `one` has the `run()` function, but a new version of `two` also adds one?




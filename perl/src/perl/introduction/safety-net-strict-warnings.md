# Safety net

* -w|options
* strict
* warnings
* diagnostics

```
#!/usr/bin/perl
use strict;
use warnings;
```

You should always use them as they are a safety net helping reduce mistakes.


It is usually very hard to add this safety net after you already have some code.


If the warnings you get don't make sense add


```
use diagnostics;
```

line and you will get more verbose warnings.




Why are use warnings and use strict so important even in small (&lt; 100 lines) scripts ?



* Help avoiding trouble with recursive functions
* Help avoiding typos in variable names
* Disable unintentional symbolic references
* Reduce debugging time
* Enable/enforce better coding standard => cleaner code, maintainability


* [Always use strict and use warnings in your perl code!](https://perlmaven.com/always-use-strict-and-use-warnings)
* [Always use warnings in your Perl code!](https://perlmaven.com/always-use-warnings)




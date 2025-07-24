# Create a test module


Now that we created the above is_any function we might want to use it in
other tests scripts as well. We might even want to distribute it to
CPAN. In order to do that we'll need to move it to a module. The accepted
name space for such modules is the Test::* namespace so we are going to
use that too.
Of course if you are building this for a specific project and not for general
use then you are probably better off using the Project::Test::* namespace
and if this is indented to be used in-house in a company then it might be better
to use Company::Test::* for the name so the chances your module will have the same
name as another module in CPAN are small.


If written correctly, the only extra thing we need to do is to
load the module and import the is_any function. Usually private test modules
are placed in the t/lib directory, so we have to add this to our @INC by
calling use lib.

{% embed include file="src/examples/test-perl/t/dice.t" %}



The problematic part is the module.
We need the **ok** and **diag** functions
from the Test::More package but we cannot load the Test::More package
as it would confuse the testing system.
So instead we are using the Test::Builder backend and the ok and diag methods
it provides.

{% embed include file="src/examples/test-perl/t/lib/Test/MyTools.pm" %}

Output:

{% embed include file="src/examples/test-perl/t/dice.out" %}



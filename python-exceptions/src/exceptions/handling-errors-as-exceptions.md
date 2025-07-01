# Handling errors as exceptions


* Only need to explicitly check for it at the level where we know what to do with the problem.
* But: Do we want our pacemaker to stop totally after missing one beat? Probably not. Or better yet: not when it is in production.

{% embed include file="src/examples/exceptions/demo4.py" %}



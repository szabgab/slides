# Uniq with List::MoreUtils

* uniq
* distinct
* List::MoreUtils


There are several ways to implement this without using an external module, but why would we want to reinvent the wheel when
there is already a good solution in the List::MoreUtils module?

The only problem, but we see it all over the programming world is that this function called "uniq" would return a list of distinct elements
instead of the ones that were unique in the original list.


* [List::MoreUtils](https://metacpan.org/pod/List::MoreUtils)

{% embed include file="src/examples/functional/uniq.pl" %}



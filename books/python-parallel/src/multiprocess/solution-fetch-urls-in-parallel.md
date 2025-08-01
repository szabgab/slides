# Solution: Fetch URLs in parallel

* First create function and use regular map.
* Deal with encoding.
* Replace continue by return, include None in results.
* It has some 2 sec overhead, but then 20 items reduced from 18 sec to 7 sec using pool of 5.

{% embed include file="src/examples/parallel/fetch_urls_multiprocess.py" %}



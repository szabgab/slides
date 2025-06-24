# Capture more

()|re
\w|re

{% embed include file="src/examples/regex/capture_more.py" %}

Some groups might match '' or even not match at all, in which case we get None
in the appropriate match.group() call and in the match.groups() call



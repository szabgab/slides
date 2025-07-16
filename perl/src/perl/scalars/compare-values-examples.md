# Compare values - examples

|  Expression      |  Value  |
|  "12.0" == 12    |  TRUE  |
|  "12.0" eq 12    |  FALSE  |
|  2 &lt; 3        |  TRUE  |
|  2 lt 3          |  TRUE  |
|  12 &gt; 3       |  TRUE  |
|  12 gt 3         |  FALSE !  |
|  "foo" == ""     |  TRUE !   (Warning) |
|  "foo" eq ""     |  FALSE     |
|  "foo" == "bar"  |  TRUE !   (Warning) |
|  "foo" eq "bar"  |  FALSE     |


When reading from STDIN you can always expect a string



{% embed include file="src/examples/scalars/is_empty_string.pl" %}



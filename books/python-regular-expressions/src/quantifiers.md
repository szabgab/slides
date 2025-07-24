# Quantifiers

* ?
* +
* *


Quantifiers apply to the thing immediately to the left of them.

In this case it is the single character `x` to the left of the quantifier, but later we'll see it can apply to a character-class or to a sub-expression enclosed in parentheses as well.
Whatever is located immediately to the left of the quantifier.



```
r'ax*a'      # aa, axa, axxa, axxxa, ...
r'ax+a'      #     axa, axxa, axxxa, ...
r'ax?a'      # aa, axa
r'ax{2,4}a'  #          axxa, axxxa, axxxxa
r'ax{3,}a'   #                axxxa, axxxxa, ...
r'ax{17}a'   #                                 axxxxxxxxxxxxxxxxxa
```
|  *  |  0-   |
|  +  |  1-   |
|  ?  |  0-1  |
|  {n,m}  |  n-m  |
|  {n,}  |  n-  |
|  {n}  |  n  |




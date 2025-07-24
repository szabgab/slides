# Quantifiers

Quantifiers apply to the thing in front of them



```
/ax*a/      # aa, axa, axxa, axxxa, ...
/ax+a/      #     axa, axxa, axxxa, ...
/ax?a/      # aa, axa
/ax{2,4}a/  #          axxa, axxxa, axxxxa
/ax{3,}a/   #                axxxa, axxxxa, ...
/ax{17}a/   #                                 axxxxxxxxxxxxxxxxxa
```

```
*      0-
+      1-
?      0-1
{n,m}  n-m
{n,}   n-
{n}    n
```


# Greedy quantifiers


{% embed include file="src/examples/regex-perl/greedy.pl" %}

```
/xa*/ on xaaab      xaaa  because it is greedy
/xa*/ on xabxaab    xa at the beginning even though the other  one is longer
/a*/  on xabxaab    the empty string at the beginning of the string
```


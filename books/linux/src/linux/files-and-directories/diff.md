# Comparing files using diff

{% embed include file="src/examples/linux/a.txt" %}
{% embed include file="src/examples/linux/b.txt" %}

```
diff a.txt b.txt
2,3c2
&lt; More text
&lt; Third line
---
&gt; Other line
```




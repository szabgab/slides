# sed - the stream editor

* sed

```
sed 's/old/new/' &lt; ORIGINAL_FILE &gt; NEW_FILE
sed 's/old/new/' ORIGINAL_FILE &gt; NEW_FILE
cat ORIGINAL_FILE | sed 's/old/new/' &gt; NEW_FILE

s/REGEX/STRING/
s:REGEX:STRING:

s/c./(&amp;)/     &amp; represent the whole match

echo fool | sed -r 's/(.)/(&amp;)/'           (f)ool
echo fool | sed -r 's/(.)\1/(&amp;)/'         f(oo)l
echo fool | sed -r 's/(.)\1/(double \1)/'     f(double o)l
```

[Sed tutorial](http://www.grymoire.com/Unix/Sed.html)




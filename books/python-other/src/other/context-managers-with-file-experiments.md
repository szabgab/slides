# Context managers: with (file) experiments

{% embed include file="src/examples/other/with_file_write.py" %}

```python
f = open('out.txt', 'w')
f.write("hello\n")
f.close()

# for line in open("myfile.txt"):
#    print line,
# the file is closed only when script ends
```





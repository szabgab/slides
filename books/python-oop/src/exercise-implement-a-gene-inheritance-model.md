# Exercise: Implement a Gene inheritance model combining DNA


* A class representing a person. It has an attribute called "genes" which is string of letters. Each character is a gene.
* Implement the `+` operator on genes that will create a new "Person" and for the gene will select one randomly from each parent.

```
a = Person('ABC')
b = Person('DEF')

c = a + b
print(c.gene) # ABF
```



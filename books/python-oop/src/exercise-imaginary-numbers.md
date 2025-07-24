# Exercise: imaginary numbers - complex numbers


Create a class that will represent imaginary numbers `(x, y*i)`
and has methods to add and multiply two imaginary numbers.


```
The math:

z1 = (x1 + y1*i)
z2 = (x2 + y2*i)
z1+z2 = (x1 + x2  + (y1 + y2)*i)

z1*z2 = x1*y1 + x2*y2*i*i + x1*y2*i + x2*y1*i
```

Add operator overloading so we can really write code like:

```
z1 = Z(2, 3)
z2 = Z(4, 7)

zz = z1*z2
```

* See [cmath](https://docs.python.org/library/cmath.html)

{% embed include file="src/examples/oop/complex_numbers.py" %}
{% embed include file="src/examples/oop/complex_numbers.out" %}



# Monkey Patching

```
import real_class
class faker(object): pass
fake = faker
real_class.time = fake
fake.sleep =
fake.time =
```

* handy in emergencies
* easily abused for NON-emergencies - gives dynamic languages a bad name
* subtle hidden "communication" via secret obscure pathways (explicit is better)

{% embed include file="src/examples/patterns/monkey.py" %}




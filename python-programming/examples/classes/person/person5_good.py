from person5 import Person

p = Person(19)
print(p.age)       # 19

p.age = p.age + 1
print(p.age)       # 20

p.birthyear = 1992
print(p.age)       # 28
   # warning: this will be different if you run the example in a year different from 2020 :)

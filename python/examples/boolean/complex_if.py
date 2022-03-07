age = 16
name = "Foo"

if 0 < age and age <= 18:
    print("age is bewteen 0 and 18")
else:
    print("age is NOT between 0 and 18")

if age < 18 or 65 < age:
    print("Young or old")
else:
    print("Working age")


if age < 18 and not name == "Foo":
    print("True")
else:
    print("False")


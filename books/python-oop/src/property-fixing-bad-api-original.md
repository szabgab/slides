# Use Python @propery to fix bad interface (the bad interface)

* @property

When we created the class the first time we wanted to have a field representing the age of
a person. (For simplicity of the example we onlys store the years.)

{% embed include file="src/examples/oop/person/person1.py" %}

Only after releasing it to the public have we noticed the problem. Age changes.

We would have been better off storing birthdate and if necessary calculating the age.

How can we fix this?



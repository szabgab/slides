# Exercise: Phone book in JSON


Write a script that acts as a phonebook. As "database" use a file in JSON format.


```
$ python phone.py Foo 123
Foo added

$ python phone.py Bar
Bar is not in the phnebook

$ python phone.py Bar 456
Bar added

$ python phone.py Bar
456

$ python phone.py Foo
123
```

* If the user provides `Bar 123` save 123 for Bar.
* If the user provides `Bar 456` tell the user Bar already has a phone number.
* To update a phone-number the user must provide `--update Bar 456`
* To remove a name the user must provide `--delete Bar`
* To list all the names the user can provide `--list`



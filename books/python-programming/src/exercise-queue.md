# Exercies: Queue


* Create file called **queue_of_people.py**

* The application should manage a queue of people.

* It will prompt the user for a new name by printing **:**, the user can type in a name and press ENTER. The app will add the name to the queue.
* If the user types in "n" then the application will remove the first name from the queue and print it.
* If the user types in "x" then the application will print the list of users who were left in the queue and it will exit.
* If the user types in "s" then the application will show the current number of elements in the queue.


```
$ python queue_of_people.py

: Joe
: Jane
: Mary
: s
  3
: n
  next is Joe
: n
  next is Jane
: Peter
: n
  next is Mary
: n
  next is Peter
: n
  the queue is empty
: Bar
: Tal
: x
  Left in the queue: Bar, Tal
$
```



# Exercise: Improve the Number Guessing game



Let the user guess several times (with responses each time) till he finds
the hidden number. Base your code on the solution from the previous exercise.
( examples/scalars/number_guessing.pl )



```
Allow the user to type
n   - skip this game and start a new one (generate new number to guess)
s   - show the hidden value (cheat)
d   - debug mode 
      (It is a toggle. 
       Pressing once the system starts to show the current
       number to guess every time before asking the user for new input
       pressing again, turns off the behavior.
       )
m   - move mode
      (It is a toggle.
       Pressing once the object will start to move a little bit after
       every step. Pressing again will turn this feature off.)
x   - exit
```


Now I can tell you that what you have is actually a 1 dimensional space fight
and you are trying to guess the distance of the enemy space ship.
As it is not a sitting duck, after every shot the spaceship can randomly move +2-2.

**Extra exercise:**

* For training purposes you might want to limit the outer space to 0-100.
* Make sure the enemy does not wander off the training field.
* Give warning if the user shoots out of space.
* Keep track of the minimum and maximum number of hits (in a file).




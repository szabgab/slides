# Exercise: MasterMind


* Create file called **mastermind.py**

* Implement the [Master Mind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) board game.

* The computer "thinks" a number with 4 different digits.
* The user guesses which digits.
* For every digit that matched both in value, and in location the computer gives a `*`.
* For every digit that matches in value, but not in space the computer gives you a `+`.
* The user tries to guess the given number in as few guesses as possible.


```
Computer:
2153       (this is hidden)

User    Response
2467    *        (because 2 is in the right place but none of the other digits match)
2715    *++      (because 2 is in the right place. 1 and 5 are used but in the wrong place. 7 not in use)
```

* [Wordle](https://en.wikipedia.org/wiki/Wordle) is basically the same game, just with letters and the extra limitation that each guess must be a valid word.




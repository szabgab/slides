# Exercies: Scripts and modules

Take the number guessing game:

If I run it as a script like this: `python game.py` then execute the whole game. Allow the user to play several games each time with a new hidden number.

If I load it as a module, then let me call the function that runs a single game with one hidden number. For example:

```
import game

game.run_game()   # will generate a new hidden number
```

We should be able to even pass the hidden number as a parameter. Like this:

```
import game

game.run_game(42)
```




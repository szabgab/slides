# Levels

* In order to make it easier or more fun to develop this game we do it step-by-step (we call them levels)

* Every level must include all the features from all the lower levels as well.

Level 0

* Using the random module the computer "thinks" about a whole number between 1 and 20.
* The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
* The game ends after just one guess.

Level 1

* The user can guess several times. The game ends when the user guessed the right number.

Level 2

* The user has some way to to leave the game without guessing the number. (e.g. press 'x' in a CLI tool)

Level 3

* The user has some way to show the hidden value (cheat). (e.g. press 's' in a CLI tool)

Level 4

* Soon we'll have a level in which the hidden value changes after each guess. In order to make that mode easier to track and debug, first we would like to have a "debug mode".
* Create a way to move the game into "debug mode": the system starts to show the current number to guess every time, just before asking the user for new input.
* Make it easy to go back to "regular mode". (e.g. in a CLI tool both can be accomplished by pressing 'd')

Level 5

* Create another toggle that will turn on/off 'move mode'. When it is 'on', the hidden number changes a little bit after every step (+/-2). That is, it is chaning by one of the following: -2, -1, 0, 1, 2. (In a CLI tool both will work by pressing 'm').

Level 6

* Let the user play several games.
* Let the user skip this game and start a new one. Generates a new number to guess. (e.g. press 'n' in a CLI tool)

Level 7

* If you have not done it yet, move the code into functions.

Level 8

* If you have not done it yet, move the code into modules

Level 9

* Save the "top score" (the lowest number of guesses).




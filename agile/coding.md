# Coding tasks
{id: coding-tasks}

## Coding Dojo - Kata
{id: coding-dojo-kata}

* Write code away from managers, deadlines, meetings, and production bug.
* Safe environment to practice and experiment.
* Simple task that can be done in a short period of time (e.g. 1-2 hours).
* Can be done multiple times in different ways (e.g. procedural vs OOP vs functional), (TDD or not), (alone, pair, mob).
* Tasks that can be used to learn a technique.



## Pair Programming
{id: pair-programming}

* There is no single right way to do it. Experiment!
* Driver - Navigator
* Driver - Navigator - Observer



## Driver-Navigator
{id: driver-navigator-observer}

* Driver writes code.
* Navigator thinks and tells the driver what to write. - The highest possible abstraction that matches the knowledge and experience level of the driver.
* The Observer is strictly observing what the current pair does.
* Sometimes neither of them know what to do. Then talk. Then suddenly one has an idea. That person becomes the navigator and the other the driver. The navigator then needs to explain the solution and the driver types it in.



## Randori
{id: randori}

* There is always a pair
* Others in the team are watching.
* Then the coder/driver goes back watching, the navigator becomes the driver and someone from the team becomes the navigator.
* Basically: Driver-Navigator-Observers



## Change of roles: when to switch?
{id: change-of-roles}

* Time boxed: fixed time (e.g. every 7 min).
* Feature boxed: When a small feature is complete.
* Ping Ping: One person writes the test(s), the other person implements the feature.
* As you feel right.



## Direction of switch?
{id: direction-of-switch}

* When there are more than 2 people, which direction to switch?
* Driver out, Navigator to Driver
* Navigator out and Driver to Navigator.



## Change of roles
{id: tdd-process}

* Write tests as well
* Work in pairs or triples
* Use git and github
* Hide your ego. Be considerate. You don't want to be criticized.


{aside}

Nor do you want your code described as shit. I think we could improve it this way. Or let's look at this other approach it might fit better. Of course we don't have a deadline so you can try both and see the relative advantages and disadvantages. 
{/aside}


## Test Driven Development - TDD
{id: test-driven-development-tdd}

* Implement the following task by always writing tests before the code, or immediately after it.
* [Testing with PyTest](https://code-maven.com/slides/python-programming/testing-with-pytest)
* [Pytest: Mocking random](https://code-maven.com/slides/python-programming/pytest-test-game-play)
* [Pytest: Capture sys](https://code-maven.com/slides/python-programming/pytest-capsys)




## One Dimensional space-fight
{id: one-dimensional-space-fight}

Level 0


* The computer generates a random whole number between 1 and 200.
* The computer prompts the user to guess.
* The user has to guess the number. After the user types in his guess the computer tells if this was bigger or smaller than the number it generated, or it was exactly that number.


Level 1


* If the user hits 'x', he can leave the game without guessing the number.



Level 2


* If the user presses 's', show the hidden value (cheat)
* If the user presses 'd' the game gets into debug mode: the system starts to show the current number to guess every time, just before asking the user for new input. Pressing 'd' again turns off debug mode. (It is a toggle.)



Level 3


* The 'm' button is another toggle. It is called 'move mode'. When it is 'on', the object move a little bit after every step (+/-2). Pressing 'm' again will turn this feature off.



Level 4


* Let the user guess several times.
* Pressing 'n' will skip this game and start a new one (generate new number to guess).



## Swapping Pairs
{id: swapping-pairs}

* Show the code to each other swapping among the pairs.





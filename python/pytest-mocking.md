# Pytest Mocking
{id: pytest-mocking}

## Pytest: Mocking - why?
{id: pytest-mocking-why}

* Testing environment that does not depend on external systems.
* Faster tests (mock remote calls, mock whole databases, etc.)
* Fake some code/application/API that does not exist yet.
* Test error conditions in a system not under our control.


## Pytest: Mocking - what?
{id: pytest-mocking-what}

* External dependency (e.g. an API).
* STDIN/STDOUT/STDERR.
* Random values.
* Methods accessin a database.


## Pytest: One dimensional spacefight
{id: pytest-number-guessing-game}

![](examples/pytest/game.py)


## Pytest: Mocking input and output
{id: pytest-test-game-exit}
![](examples/pytest/test_game_exit.py)


## Pytest: Mocking random
{id: pytest-test-game-play}
![](examples/pytest/test_game_play.py)


## Pytest: Mocking slow external API call
{id: pytest-mocking-slow-external-call}

![](examples/pytest/external-api/mymath.py)
![](examples/pytest/external-api/externalapi.py)
![](examples/pytest/external-api/use_mymath.py)

![](examples/pytest/external-api/test_mymath.py)
![](examples/pytest/external-api/test_mymath_broken_remote.py)


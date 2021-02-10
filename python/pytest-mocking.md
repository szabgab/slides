# Pytest Mocking
{id: pytest-mocking}

## Test Doubles
{id: test-doubles}

* Dummies
* Spies
* Stubs
* Fakes
* Mocks
* (Gerard Meszaros)


## Monkey Patching
{id: pytest-monkey-patching}



## Pytest: Mocking - why?
{id: pytest-mocking-why}

* Testing environment that does not depend on external systems.
* Faster tests (mock remote calls, mock whole databases, etc.)
* Fake some code/application/API that does not exist yet.
* Test error conditions in a system not under our control.

* TDD, unit tests
* Spaghetti code
* Simulate hard to replicate cases
* 3rd party APIs  or applications

## Pytest: Mocking - what?
{id: pytest-mocking-what}

* External dependency (e.g. an API).
* STDIN/STDOUT/STDERR.
* Random values.
* Methods accessing a database.
* Time.
* Hard-coded path

## Pytest: Hard-coded path
{id: pytest-hard-coded-path}

![](examples/pytest/hard-coded-path/app.py)
![](examples/pytest/hard-coded-path/test_app.py)
![](examples/pytest/hard-coded-path/test_app_monkeypatch.py)

## Pytest: Mocking slow external API call
{id: pytest-mocking-slow-external-call}

![](examples/pytest/external-api/mymath.py)
![](examples/pytest/external-api/externalapi.py)
![](examples/pytest/external-api/use_mymath.py)

![](examples/pytest/external-api/test_mymath.py)
![](examples/pytest/external-api/test_mymath_broken_remote.py)

## Pytest: Mocking STDIN
{id: pytest-mocking-stdin}

![](examples/pytest/stdin/app.py)
![](examples/pytest/stdin/use_app.py)
![](examples/pytest/stdin/test_one.py)
![](examples/pytest/stdin/test_two.py)

## Pytest: Mocking random numbes
{id: pytest-mocking-random-numbers}

![](examples/pytest/random/app.py)
![](examples/pytest/random/test_app.py)

## Pytest: Mocking multiple random numbers
{id: pytest-mocking-multiple-random-numbers}

![](examples/pytest/random-more/app.py)
![](examples/pytest/random-more/use_app.py)
![](examples/pytest/random-more/test_app.py)

## Pytest: Mocking time (test expiration)
{id: pytest-mocking-time-test-expiration}

![](examples/pytest/time-passed/app.py)
![](examples/pytest/time-passed/test_app.py)


## Pytest: monkeypatching time
{id: pytest-monkeypatching-time}

![](examples/pytest/time-changed/app.py)
![](examples/pytest/time-changed/test_impact.py)
![](examples/pytest/time-changed2/app.py)
![](examples/pytest/time-changed2/test_impact.py)
![](examples/pytest/time-changed2/test_impact_monkeypatch.py)

## Pytest: One dimensional spacefight
{id: pytest-number-guessing-game}

![](examples/pytest/game.py)


## Pytest: Mocking input and output
{id: pytest-test-game-exit}

![](examples/pytest/test_game_exit.py)


## Pytest: Mocking random
{id: pytest-test-game-play}

![](examples/pytest/test_game_play.py)


## Pytest: Mocking Flask app sending mail
{id: pytest-mocking-flask-app-sending-mail}

![](examples/pytest/mocking-flask/app.py)
![](examples/pytest/mocking-flask/test_app.py)

## Pytest: Mocking - collecting stats example
{id: pytest-mocking-collecting-stats}

![](examples/pytest/monkey-collect/app.py)



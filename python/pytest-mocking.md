# Pytest Mocking
{id: pytest-mocking}

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

* Hard-coded path in code.
* STDIN/STDOUT/STDERR.
* External dependency (e.g. an API).
* Random values.
* Methods accessing a database.
* Time.

## Pytest: What is Mocking? - Test Doubles
{id: pytest-test-doubles}

* Dummies
* Spies
* Stubs
* Fakes
* Mocks
* [Test Doubles by Gerard Meszaros and Martin Fowler](https://martinfowler.com/bliki/TestDouble.html)

## Pytest: Monkey Patching
{id: pytest-monkey-patching}

* [Monkey Patch](https://en.wikipedia.org/wiki/Monkey_patch)
* In Pytest: The name of the fixture to do mocking is [monkeypatch](https://docs.pytest.org/en/stable/monkeypatch.html)

## Pytest: Hard-coded path
{id: pytest-hard-coded-path}

![](examples/pytest/hard-coded-path/app.py)

## Pytest: Hard-coded path - manually replace attribute
{id: pytest-hard-coded-path-manually-replace}

![](examples/pytest/hard-coded-path/test_app.py)

## Pytest: Hard-coded path - monkeypatch attribute
{id: pytest-hard-coded-path-monkyepatch}
{i: monkeypatch}
{i: setattr}

![](examples/pytest/hard-coded-path/test_app_monkeypatch.py)

## Pytest: Hard-coded path - monkeypatch attribute - tempdir
{id: pytest-hard-coded-path-monkyepatch-tempdir}
{i: monkeypatch}
{i: setattr}
{i: tmpdif}

![](examples/pytest/hard-coded-path/test_app_monkeypatch_tempdir.py)


## Pytest: Mocking slow external API call
{id: pytest-mocking-slow-external-call}

![](examples/pytest/external-api/mymath.py)
![](examples/pytest/external-api/externalapi.py)
![](examples/pytest/external-api/use_mymath.py)

## Pytest: Mocking slow external API call - manually replace function
{id: pytest-mocking-slow-external-call-manually-replace}

![](examples/pytest/external-api/test_mymath.py)

## Pytest: Mocking slow external API call - manually replace function - broken remote
{id: pytest-mocking-slow-external-call-manually-replace-broken-remote}

![](examples/pytest/external-api/test_mymath_broken_remote.py)

## Pytest: Mocking slow external API call - monkeypatch
{id: pytest-mocking-slow-external-call-monkeypatch}

![](examples/pytest/external-api/test_mymath_monkeypatch.py)


## Pytest: Mocking STDIN
{id: pytest-mocking-stdin}

![](examples/pytest/stdin/app.py)
![](examples/pytest/stdin/use_app.py)

## Pytest: Mocking STDIN manually mocking
{id: pytest-mocking-stdin-manually-mocking}

![](examples/pytest/stdin/test_one.py)
![](examples/pytest/stdin/test_two.py)

## Pytest: Mocking STDIN - monkeypatch
{id: pytest-mocking-stdin-monkeypatch}

![](examples/pytest/stdin/test_both_monkeypatch.py)

## Pytest: Mocking random numbes - the application
{id: pytest-mocking-random-numbers-the-application}

![](examples/pytest/random/app.py)

## Pytest: Mocking random numbes
{id: pytest-mocking-random-numbers}

![](examples/pytest/random/test_app.py)

## Pytest: Mocking multiple random numbers
{id: pytest-mocking-multiple-random-numbers}

![](examples/pytest/random-more/app.py)
![](examples/pytest/random-more/use_app.py)
![](examples/pytest/random-more/test_app.py)

## Pytest: Mocking environment variables
{id: pytest-mocking-environment-variables}

![](examples/pytest/setenv/app.py)
![](examples/pytest/setenv/test_app.py)

## Pytest: Mocking time
{id: pytest-mocking-time}

There are several different problems with time

* A login that should expire after 24 hours. We don't want to wait 24 hours.
* Some code that must be executed on certain dates. (e.g. January 1st every year)


## Pytest: Mocking time (test expiration)
{id: pytest-mocking-time-test-expiration}

{aside}
In this application the user can "login" by providing their name and then call the `access_page` method within  `session_length` seconds.

Because we know it internally users the `time.time` function to retreive the current time (in seconds since the epoch) we can
replace that function with ours that will fake the time to be in the future.
{/aside}

![](examples/pytest/time-passed/app.py)
![](examples/pytest/time-passed/test_app.py)

## Pytest: mocking specific timestamp with datetime
{id: pytest-mocking-specific-time-in-datetime}

{aside}
This function will return one of 3 strings based on the date: `new_year` on January 1st,
`leap_day` on February 29, and `regular` on every other day. How can we test it?
{/aside}

![](examples/pytest/specific-time/app.py)
![](examples/pytest/specific-time/use_app.py)

## Pytest: mocking specific timestamp with datetime
{id: pytest-mocking-specific-time-in-datetime-monkeypatch}

![](examples/pytest/specific-time/test_app.py)

## Pytest: mocking datetime.date.today
{id: pytest-mocking-datetime-date-today}

{aside}
The datetime class has other methods to retreive the date (and I could not find how to mock the function deep inside).
{/aside}

![](examples/pytest/mock-get-today/app.py)
![](examples/pytest/mock-get-today/use_app.py)
![](examples/pytest/mock-get-today/test_app.py)


## Pytest: mocking datetime date
{id: pytest-mocking-datetime-date}

![](examples/pytest/years-passed/app.py)
![](examples/pytest/years-passed/use_app.py)
![](examples/pytest/years-passed/test_app.py)

## Pytest: One dimensional spacefight
{id: pytest-number-guessing-game}

![](examples/pytest/game/game.py)


## Pytest: Mocking input and output in the game
{id: pytest-test-game-exit}

![](examples/pytest/game/test_game_exit.py)

## Pytest: Mocking input and output in the game - no tools
{id: pytest-test-game-exit-no-tools}

![](examples/pytest/game/test_game_exit_bare.py)


## Pytest: Mocking random in the game
{id: pytest-test-game-play}

![](examples/pytest/game/test_game_play.py)

## Pytest: Mocking random in the game - no tools
{id: pytest-test-game-play-no-tools}

![](examples/pytest/game/test_game_play_bare.py)


## Pytest: Mocking Flask app sending mail
{id: pytest-mocking-flask-app-sending-mail}

![](examples/pytest/mocking-flask/app.py)
![](examples/pytest/mocking-flask/test_app.py)

## Pytest: Mocking - collecting stats example
{id: pytest-mocking-collecting-stats}

![](examples/pytest/monkey-collect/app.py)



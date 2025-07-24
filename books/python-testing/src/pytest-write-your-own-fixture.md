# PyTest - write your own fixture

* `tmpdir` and `capsys` are nice to have, but we will need more complex setup and teardown.

* We can write any function to become fixture, we only need to decorate it with `@pytest.fixture`

* We can implement fixture functions to act like the xUnit fixture we saw ealrier or using dependency injection as `tmpdir` and `capsys` work.




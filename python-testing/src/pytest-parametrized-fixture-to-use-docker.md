# Pytest parametrized fixture to use Docker

I created a GitHub Action for the [OSDC site generator](https://github.com/OSDC-Code-Maven/osdc-site-generator) which is running inside a Docker container.
At one point I wanted the whole image creation and running in the image be part of the test.

{% embed include file="src/examples/pytest/test_parametrized_fixture_with_docker.py" %}



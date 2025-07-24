# Minimal Travis-CI echo

The first thing we can do is specify some code to run in the environment. For this we need to add the `script` field to the YAML file with a command.
A simple one would be just to `echo` some text.

If we make this change in the GitHub editor then immediately after you commit the change it will trigger a new build on Travis-CI. If you edit the file
locally on your computer, then you need to commit the change and push it out to GitHub. In this case the `push` operation will trigger the
build on Travis-CI.


{% embed include file="src/examples/minimal-echo/.travis.yml" %}



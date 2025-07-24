# Exercise: improve the color selector

Take the examples/perlarrays/process_command_line.pl
script and improve it in several ways:

1. Check if the value given on the command line is indeed one of the possible values and don't let other colors pass.
1. Allow a --force flag that will disregard the previously implemented restriction. Meaning 
1. **--color Purple** should still report error but
1. **--color Purple --force** should accept this color as well.



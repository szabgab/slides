# How "import" and "from" work?


* import

1. Find the file to load.
1. Compile to bytecode if necessary and save the bytecode if possible.
1. Run the code of the file loaded.
1. Copy names from the imported module to the importing namespace.



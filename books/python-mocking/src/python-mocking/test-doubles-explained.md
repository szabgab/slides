# Test Doubles explained



Dummy objects are passed around but never actually used.

Fakes - Working implementation, but much more simple than the orignial.
* An in-memory list of username/password pairs that provide the authentication.
* A database interface where data stored in memory only, maybe in a dictionary.

Mocks - Mocks are objects that register calls they receive, but do not execute the real system behind.

Stubs - Stub is an object that holds predefined data and uses it to answer calls during tests.
* A list of "random values".
* Responses given to prompt.

Spies usually record some information based on how they were called and then call the real method. (or not)



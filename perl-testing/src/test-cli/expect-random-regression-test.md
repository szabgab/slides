# Random regression tests

The idea is that we don't have time to manually setup hundreds of tests and calculate our expectations
so instead we compare some random tests to the results of a previous run.


We can log the results of each operation in a file and compare
the resulting files to some previous execution.

* Create a set of random operations
* Because we don't have time to check all the results we only check if there were no error messages, but in general we don't care about the correctness of the results
* Record the tests and the results
* Run the tests again with the a version (now they are not random any more) and check if any of the results has changed. If something changed it indicates that either earlier or now we have a problem
* Investigate the differences and include the problematic tests in the manual test suit
* Either save the new results as the new expectation or discard it and discard the current version of the application


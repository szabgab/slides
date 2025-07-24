# prove --state


* prove --state=save          will save the status of the meta data of the test run in .prove
* prove --state=failed        will run the test scripts that failed last time (based on .prove)
* prove --state=failed,save   run the failed tests and update .prove
* prove --shuffle --state=save  Run in random order and save it in .prove
* prove --state=last            Run the same order as last time (the result of shuffle)
* prove --state=todo            Run the test scripts with TODO entries
* prove --state=slow -j4        Run the slowest test first (but then 4 in parallel)




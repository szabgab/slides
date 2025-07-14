# Integrated feature branches


* Commit back (See Generate GitHub Pages)

* Don't allow direct commit to "prod"
* Every push to a branch called /release/something  will check if merging to "prod" would be a fast forward, runs all the tests, merges to "prod" starts deployment.



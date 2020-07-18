# Testing Intro
{id: testing-intro}

## The software testing equasion
{id: software-testing-equasion}

```
INPUT + PROCESS = EXPECTED_OUTPUT
```


## The software testing equasion (fixed)
{id: software-testing-equasion-revised}

```
INPUT + PROCESS = EXPECTED_OUTPUT + BUGS
```



## The pieces of your software?
{id: pieces-of-your-software}

* Web application with HTML interface?
* Web application with HTML + JavaScript? Which frameworks?
* Web application with JSON interface? (API)
* What kind of databases do you have in the system? SQL? NoSQL? What size is the database?
* Source and the format of your input? Zip? CSV? XML? SQL Dump? JSON?
* The format of your output? HTML/PDF/CSV/JSON/XML/Excel/Email/..?
* Are you pushing out your results or are your cliens pulling them? e.g. via an API?
* What external dependencies do you have? Slack, Twilio, What kind of APIs?



## Manual testing
{id: manual-testing}

* How do you check your application now?



## What to tests?
{id: what-to-test}

* Happy path
* Sad path



* Valid input
* Valid edge cases (0, -1, empty string, etc.)
* Broken input (string instead of number, invalid values, too long input, etc.)
* Extreme load
* System failure (power failure, network outage, lack of memory, lack of disk, ...)
* Third-party error or failure - How does your system work if the 3rd party API returns rubbish?



## Continuous Integration
{id: continuous-integration}

* Reduce feedback cycle
* Avoid regression
* On every push
* Every few hours full coverage







# Notes

## Topics around software engineering

* Continuous Delivery
* TDD
* BDD
* Micro services
* Continuous integration
* Extreme programing
* Software design and archiecture


* Fast feedback loop
* Testing

### Pull Requests + Code review vs Continuous Integration?

* [Why Pull Requests Are A BAD IDEA](https://www.youtube.com/watch?v=ASOSEiJCyEM)
* [DORA](https://dora.dev/)

* Pull-Requests (+ Code Review) works great in Open source where the participants work asynchronous, probably don't know each other. Can't fully trust most of the contributors, and are not working on the same project all the time.

* For companies it might not be such a great way.
* pair programming?


### Feature branching

For many years the central problem of version control systems was that they did not provide good branching tools. Actually branching wasn't the real problem, merging was. However without good merging, branching was really a pain.
With the popularity of git marging and thus branching got a lot easier which lead to the made feature branching a lot more popular than before.
However, feature branching also has drawback. In particular it has a huge tension with the idea of Continuous Integration and thus with Continuous Delivery.

* [Why CI is BETTER Than Feature Branching](https://www.youtube.com/watch?v=lXQEi1O5IOI)
* [Continuous Integration vs Feature Branch Workflow](https://www.youtube.com/watch?v=v4Ijkq6Myfc)



### Fast feedback loop



### How to know your software works correctly?

We write software because we would like to make sure it does something useful without errors. The big question is of course how do we know our software works.
Ultimately the question boils down to whether the user (customer, client, whatever word you use there) is satisfied.  BDD Acceptance testing


### Writing automated test





### Estimates and why are they always wrong?

* [Why Software Estimations Are Always Wrong](https://www.youtube.com/watch?v=OS6gzabM0pI)

* Estimates are basically guesses about the future.

* We interested in the estimates as we would like to decide what do next and/or we would like to estimate the cost of something, or that we might need to synhronize other actions (e.g. marketing) with the completion of a feature.

* How long does it take to pull a tooth? Dentist know how much time to allocate for it as they have done this thousans of time, but still there is a variation. So they allocate enough time.
(The estimates  got:

* Numbing the area: 5-10 minutes
* Loosening and extracting the tooth: 5-15 minutes (depending on the tooth)
* Cleaning and closing the site (if needed): 5-10 minutes

As we can see even for a fairly stadard operation the variation is quite high.

* How long does it take to build a road?
While the people building a road - at least the leaders - have probably already built a few roads the estimates are still difficult.
There are a lot of similar things between different roads, but also each road has some unique aspects. You also need to take in account accidents, external factors.
The possibility to find something in the ground that makes you stop building for a while. (e.g. you bump into some archeological findings.)
These days you might be able to scan the ground ahead of the construction,  but in older time even the  quality of the ground was not well know before construction began.

* HiPPO - Highest paid person’s opinion (The traditional way of decision making)

* We would like to create the **Most value for the least amount of work**

* A made-up word often used to descripe the process is **guesstimate**.

Planning is structured guessing

Cost of Delay
CD3    Cost of Delay / Duration




- Goals of companies and people
- Waterfall model, what are the problems with it? (What are the costs and risks?)


Run ./value/time_value.py  to generate the drawings.
View them at: file:///Users/gabor/work/slides/value/svg.html

## About you
{id: about-you}

* Name
* Company
* What do you do?
* What kind of products and services do you develop?
* Something interesting about you.

Introduction to DevOps

* Automation, CI/CD, XP, ...

Alternative titles:
How to develop software faster and have more stable releases?

* How to create better software faster at a lower price while keeping the employees happy?

## Subtitles
{id: subtitles}

* Faster cheaper better pick any 3
* Fast cheap low-risk
* Predictable software development

## ITIL
{id: itil}

* ITIL - Information Technology Infrastructure Library.
* ITSM - IT service management.

## Two
{id: two-}

Systems of record (needs to be stable)
Systems of engagement (needs to change fast)


Continuous Improvement
Continuous Learning

Refactoring to minimize complication

Goal - Value

* What is our goal?
* Why are we here?

## Values
{id: values}

* More value to customer


Time is Money

* Putting a name on it marking with a v does not work well.
* Better to discuss what can and what cannot make a difference.

Development velocity

## The tension
{id: the-tension}

Fast development and stable software are traditionally seen as orthogonal to each other.

However research shows that using the right approach one can achieve fast-paced development and stable software.
(See the DevOps handbook.)

Two competing goals of the IT organization:

* Respond to the rapidly changing competitive landscape. (Development)
* Provide stable, reliable, and secure service to the customer. (Operations)

A special case of the above mentioned problem is the tension between developers and operations.
Traditionally Developers are more interested in creating software, using the latest libraries etc.
Operations are required to provide stability for the production system. Stability requires little or no changes to the software stack. (e.g. OS, third-party library, code)


## Deploy per day VS stability
{id: deploy-per-day-vs-stability}

A drawing: x coordinates risk of release (number of issues per release, stability of release)
y coordinates: frequency of releases. (The paradox)

Getting faster
A drawing of an arrow or just line. On the left side it is "an organization that releases software once a year"
on the right end "Amazon, releasing once a second".
Move further to the right on this line.


* [Wakatime](https://wakatime.com/)


## Value stream (a concept of lean)
{id: value-stream}

Value stream mapping: how to visualize work and align leadership for organizational transformation. 

From idea (hypothesis, request) to solution running in production.


## The Flow
{id: flow}

* Flow of information and material.
* Value is only realized when the feature reaches the customer.

* Requirements (Product management)
* Design
* Development
* Information security (InfoSec)
* QA
* IT Operations

## Improve the Value stream
{id: improve-the-values-stream}

* Make the work and the bottlenecks visible!  Eg use a Kanban board.
* Limit work in process (WIP), as that only generates cost. (Fewer Things, More Done)
* Reduce switching cost, wasted investment.
* Reduce batch sizes
* Reduce number of handoffs as each handoff is a queue. A source for misunderstanding etc. Functional testing load testing firewall, server setup etc.  Solution is automation and more autonomous teams self service teams. 
* Continually Identify and remove our bottlenecks.
* Constantly optimizing the system.
* Preventing rework. Reduce the number and seriousness of defects.
* Eliminate waste and hardship

## Total time
{id: total-time}

* Time to complete a task from requirement to use by client.

## Lead time
{id: lead-time}

* Lead time: Time between check-in of the code till it is deployed and used.
* Lead time: part of the value stream starts when the solution was checked in to version control. 
* Long lead time is for large complex tightly coupled monolithic projects.
* Reduce WIP: Kanban board can be used.
* Reduce batch size.


## Objectives
{id: objectives}

* Reduce the risk associated with large releases.
* Increase the ability to release features fast to beat the competition.
* Increase the ability to scale.
* Increase trust between development and operations

## Management
{id: management}

* Management is good if you need complience.
* For engagement, self-direction works better.


The best way to learn something is to explain it to others. So make it a regular practice in your team to learn new things and explain them to each other.

-----
There is no conceptual difference between automated unit~, integration~, and acceptance~ tests. They all have the same formula:

f(input) == expected output + bugs

Only the size of f() is different.
-----
There is no such thing "writing regression tests". You write unit~, integration~, or acceptance~ tests and when you run it for the second time after changing the application then it becomes a regression test.
-----
Gated check-in systems are a hindrance to fast-pased development. They only slow down developers and make them game the system. Do you require an open ticket for every commit? Good, now we can't even fix a typo without approval. Trust your developers!

Good, now we cannot fix a typo and changing a variable name from $data to $value will cost us a lot and thus we'll never do it.

Q: How gated check-in builds affect your team?
A: They make them slow and hate your guts.

Trust your developers!
----
Frequent commits, short lived branches, tests always passing.
----


Cases:
* New company, with 5 developers + 2 qa person. Release once a week.
   "We will need DevOps, but not now."
* Compile time of the software is 30 minutes
* Person writes some feature. QA checks it 3 months later and reporst about bugs.


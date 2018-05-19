# Introduction to DevOps
{id: index}

## Subtitles
{id: subtitles}

* Faster cheaper better pick any 3
* Fast cheap low-risk
* High-performing technology organizations.

## Goal - Value
{id: goal}

* What is our goal?
* Why are we here?

The overall goal of the companies is to create more value to customers.

## Time
{id: time}

* The sooner the better.

* Getting 1,000,000 ten years from now is great.
* Getting it one year from now is much better.
* Getting it next week is even better than that.

So "sooner" has a higher value than later.

"Time is Money"

## What is the solution
{id: what-is-the-solution}

* Lean
* Agile
* Scrum
* Kanban
* SAFe
* Spine
* XP
* DevOps
* DevSecOps

* Stamping a name on it marking with a v does not work well.
* Better to discuss what can and what cannot make a difference.

## Fast or stable?
{id: fast-or-stable}

Fast development and stable software are traditionally orthogonal to each other.

However research shows that using the right approach one can achieve fast-paced development and stable software.
(See the DevOps handbook.)

## Deploy per day VS stability
{id: deploy-per-day-vs-stability}

A drawing: x coordinates risk of release (number of issues per release, stability of release)
y coordinates: frequency of releases. (The paradox)


## The tension
{id: the-tension}

Two competing goals of the IT organization:

* Respond to the rapidly changing competitive landscape. (Development)
* Provide stable, reliable, and secure service to the customer. (Operations)

A special case of the above mentioned problem is the tension between developers and operations.
Traditionally Developers are more interested in creating software, using the latest libraries etc.
Operations are required to provide stability for the production system. Stability requires little or no changes to the software stack. (e.g. OS, third-party library, code)

## Getting faster
{id: getting-faster}

A drawing of an arrow or just line. On the left side it is "an organization that releases software once a year"
on the right end "Amazon, releasing once a second".
Move further to the right on this line.

## Wall of Confusion
{id: wall-of-confustion}

![Wall of Confusion](WallOfConfusion.png)

by Andrew Clay Shafer.

( source: http://dev2ops.org/2010/02/what-is-devops/ )

## Priorities
{id: priorities}

* Instaed of building 5 features - one feature each person
* Build 2-3 features first and when you are done build the remaining feature.

* You get some value (and feedback) earlier.
* Incremental delivery.

## Test-Driven Development
{id: test-driven-development}

* Tests provide a solid ground to run on.
* More confidence in our changes.
* Tests make better code.
* Tests make better systems (catch bugs earlier).

## Optimizing Developer Effort
{id: optimizing-developer-effort}

Microsoft research shows that developers on a mature code-base spend their time:

* 75% reading code
* 20% modifying code
* 5% writing new code

* [source](https://blogs.msdn.microsoft.com/peterhal/2006/01/04/what-do-programmers-really-do-anyway-aka-part-2-of-the-yardstick-saga/)
* [Wakatime](https://wakatime.com/)


## The business cost
{id: the-business-cost}

* Wasted time, cost fixing bugs.
* Low of customer trust due to bugs.
* Long development time.
* Fear of release.


## The human cost
{id: the-human-cost}

* Long working hours.
* Reduced quality of life.
* Powerless in the organization.
* Low employee satisfaction.
* High turnover rate.

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

## Small Batch size
{id: small-batch-size}

Example: fill envelops - you have 10 envelops to fill with a letter. You have 4 steps

* Fold the letter.
* Put the letter in the envelop.
* Write the address on the envelop.
* Seal the envelop.


## Reduce Multitasking
{id: reduce-multitaskin}

Drawing thats shows how much time we spend on actual work vs. The switching cost for 1-5 parallel tasks.

![Multitasking](multitasking.png)

(source http://flowa.fi/blog/2014/10/23/games-to-learn-kanban-why-and-how.html )

## Multitasking Exercise
{id: multitasking-exercise}

Exercise: Write down 3 sets of values while measuring the time to get the following results:

```
0  1   2  3  4   5    6     7   8  9
a  b   c  d  e   f    g     h   i  j
I II III IV  V  VI  VII  VIII  IX  X
```

First time write these horizontally:

* First write down the Arabic numbers.
* Then the Latin letters
* Then the roman numbers.

In the next round write the same ones down, but this time start by writing down the first value of each, then the second value of each. (So you'd first write down 0, a, I, then 1, b, II etc.)

Observe how much longer the second method takes.

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

## Conway's Law
{id: conways-law}

* Mel Conway 1967

* Organization determines architecture

* Modulare system requires modular organization

## Small Teams
{id: small-teams}

* 2 Pizza team (Jeff Bezos) (Full-service)
* Align to Business Domains

## Project boundaries
{id: project-boundaries}

* The majority of the work should be inside of each team.

## Build only what you need
{id: build-only-what-you-need}

* When asked to add a feature, first try to figure out Why ? What is the problem that needs to be solved?
* If possible use an existing tool or service. (Open Source, Cloud)
* Focus on building what you really need.


## Daily feedback meetings
{id: daily-feedback-meetings}

* What did you finish yesterday?
* What will you finish today?
* What's blocking you? ( What's your red flag? )

## Objectives
{id: objectives}

* Reduce the risk associated with large releases.
* Increase the ability to release features fast to beat the competition.
* Increase the ability to scale.
* Increase trust between development and operations

## Feedback Techniques
{id: techniques}

* Create fast feedback loops

* Test automation (unit and other autometed tests).
* Build system.
* Continuous Integration (CI).
* Continuous Deployment (CD).
* Code reviews.
* Pair programming.
* Mob programming.
* Telemetry: servers, client interaction, errors, failures... Log and monitor everything. 
* Swarm and solve problems, build and spread new knowledge. Toyota Andon cord. 

## Fast feedback
{id: fast-feedback-loop}

* Learning from mistakes made half a year earlier is costly, painful, and never really happens.
* Learning from mistakes made 10 min ago is much more valuable.

## What is in there for me, the developer?
{id: what-is-in-there-for-the-developer}

Most engineers I know want to enjoy work and be proud of their accomplishments. 

* Safer work place - no fear of change, no fear of release.
* Better working environment. 
* Much less bugs and rework of the same code. 
* Allow you to do other work when this is done
* Learn better development practices that will be relevant in your next job as well.


## Features
{id: features}

* Testability
* Deployability
* Architecture
* Security
* Performance
* Stability
* Configurability


## The DevOps transformation process
{id: devops-transformation-process}

* Pick the value stream to be the first to convert

## Resilient teams
{id: resilient-teams}

* Chaos Monkey of Netflix
* Randomly kill processes and compute servers in production to see how the monitoring system and the whole team reacts
* Do this often during work hours and reduce the risk of such thing happening during the nights.

## Release frequency
{id: release-frequency}

![Release frequency](release-frequency.jpg)

(source https://medium.com/data-ops/releasing-new-analytics-every-second-fc5fefd92360 )

## DevOps loop
{id: devops-loop}

![DevOps loop](devops-300x148.png)

* Requirements
* Design / Plan
* Development  / Code
* Build
* InfoSec
* QA
* Release
* Deploy
* Operations
* Monitoring

## End-to-end Ownership
{id: end-to-end-ownership}

* You build it, you run it. Werner Vogels  (CTO of Amazon)

The same team

* writes code
* checks quality
* runs the service

* If you are the one who needs to wake up at night for a bug, you will fix it soon.


## Continuous Integration (CI)
{id: continuous-integration}

* Repeatable deployment pipeline.

## Design
{id: design}

* Design for both external and internal customers. 
* The external pays for it but the internal also uses it. 
* Optimize for downstream work center. 

## How to implement all this?
{id: how-to-implemnt}

* Top down support.
* Bottom up experimentation, feedback. 

* Get support from the top: VP RnD, CxO.
* Team level.

## Theory X and Theory Y
{id: theory-x-and-theory-y}

* X thinks people are lazy, need supervision.
* Y thinks people can be autonomous if trusted.

* [Theory X and Theory Y](https://en.wikipedia.org/wiki/Theory_X_and_Theory_Y)

## Time boxing experiment
{id: time-boxing-experiment}

* Use time boxing for experimentation to reduce risk and increase chances of acceptance. 

## Greenfield projects VS brownfield projects
{id: brownfield-projects}

Greenfield projects are easier to get started with.

Brownfield projects have:

* Technical debt.
* Legacy code.
* Unsupported platforms.

* Users.


## Top down approach
{id: top-down-approach}

* Start with the team that has the most open attitude to the new way of work. 
* Educate people. Both about the ideas and about the techniques.
* Find the first bottleneck that is in your power to change.
* Reinforce learning culture.
* Instead of adding more people to the team, improve the way the team works.

## Team level approach
{id: team-level-approach}

* Start writing tests.
* For every new feature, for every bug.
* Include time for refactoring.

At first this will take you extra time. Later you will see the value. Put it in the estimates. They are part of your job.

* Allocate at least 20% of your time to this.


## Implementation
{id: implementation}

* Infrastructure as code.

The two most important aspects are value creation and feedback. So start with this. Discuss the things we value. Then build in short feedback loops in your process. 

## Learn from the mistakes
{id: learn-from-the-mistakes}

* Blameless post mortem. [Etsy Morgue tool](https://github.com/etsy/morgue).
* Learning organization.
* Transform local discoveries into global improvements. ( US navy reactors. )

## Resilience testing
{id: resilience-testing}

* Intentianlly cause problems during the work day and see how the tools and the team react.
* Fix any issues. Learn.
* [Netflix Chaos Monkey](https://github.com/Netflix/SimianArmy/wiki/Chaos-Monkey)


## Resources
{id: recommended-books}

* [The Phoenix project](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/0988262592)
* [The DevOps handbook](https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002/)
* [Continuous delivery](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912/) by Jez Humble and Dave Farley
* [Lean Software Development: An Agile Toolkit](https://www.amazon.com/Lean-Software-Development-Agile-Toolkit/dp/0321150783) by Mary Poppendieck and Tom Poppendieck.
* [The Goal: A Process of Ongoing Improvement](https://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271951) by Eliyahu M. Goldratt and Jeff Cox.
* [Lean Thinking: Banish Waste and Create Wealth in Your Corporation](https://www.amazon.com/Lean-Thinking-Corporation-Revised-Updated/dp/0743249275) by James P. Womack and Daniel T. Jones.
* [The Fifth Discipline: The Art & Practice of The Learning Organization](https://www.amazon.com/Fifth-Discipline-Practice-Learning-Organization/dp/0385517254) by Peter M. Senge.
* [Beyond Legacy Code](https://pragprog.com/book/dblegacy/beyond-legacy-code) by David Scott Bernstein.

* [Velocity and volume (or speed wins)](https://www.youtube.com/watch?v=wyWI3gLpB8o) Adrian Cockcroft.
* [Moving Fast At Scale](https://www.youtube.com/watch?v=oH4g7wLPqg4) Randy Shoup.



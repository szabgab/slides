# Introduction to DevOps
{id: introduction-to-devops}

## Goal
{id: goal}

* What is our goal?
* Why are we here?

The overall goal of the companies is to create more value to customers in order to get more value out of it.

If the same amount received today has a higher value than a year from now. So "sooner" has a higher value than later.

## Business needs for change
{id: business-needs-for-change}

* Reduce time to market
* Increase feature throughput

* Decrease cost
* Increase quality

## Fast or stable?
{id: fast-or-stable}

Fast development and stable software are traditionally orthogonal to each other.

However research shows that using the right approach one can achieve fast-paced development and stable software.  (Research ?)

A special case of the above mentioned problem is the tension between developers and operations.
Traditionally Developers are more interested in creating software, using the latest libraries etc.
Operations are required to provide stability for the production system. Stability requires little or no changes to the software stack. (e.g. OS, third-party library, code)

## Flow
{id: flow}

* Requirements
* Design
* Development
* InfoSec
* QA
* Operations

## Improve the Value stream
{id: improve-the-values-stream}

* Small batch size.
* Reducing work in process (WIP) as that only generates cost.
* Preventing rework. Reduce the number and seriousness of defects.
* Constantly optimizing the system.


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

## Lead time
{id: lead-time}

* Time to complete a task from requirement to use by client. 
* Lead tine: from time of check-in till use of the code. 
* Reduce WIP: Kanban board can be used. 
* Reduce batch size. 

## Daily feedback meetings
{id: daily-feedback-meetings}

* What did you finish yesterday?
* What will you finish today?
* What's blocking you? ( What's your red flag? )

## Techniques
{id: techniques}

* Fast feedback loop
* Test automation
* Continuous Integration (CI)
* Continuous Deployment (CD)
* Code reviews
* Pair programming
* Monitoring

## Greenfield projects VS brownfield projects
{id: brownfield-projects}

* Technical debt
* Legacy code
* Unsupported platform

## Features
{id: features}

* Testebility
* Deployability


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


## ITIL
{id: itil}

* ITIL - Information Technology Infrastructure Library
* ITSM - IT service management 


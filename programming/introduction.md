# Introduction to Programming
{id: programming-intro}

## Computer Hardware Architecture
{id: computer-hardware-architecture}
{i: CPU}

* [Computer Hardware](https://en.wikipedia.org/wiki/Computer#Hardware)
* [CPU -  Central Processing Unit](https://en.wikipedia.org/wiki/Central_processing_unit) (Single core, multi-core), (clock speed in GHz), instruction set (386, Pentium, i3, i7, ...) 
* [RAM -  Random Access Memory](https://en.wikipedia.org/wiki/Random-access_memory) (in phones a few Gbs, in PCs 4-16 Gb, in servers it can reach a few hundred Gbs as well)
* [Hard disk](https://en.wikipedia.org/wiki/Hard_disk_drive) (spinning disks or [SSD - Solid State Drive](https://en.wikipedia.org/wiki/Solid-state_drive)) - Phone: 16, 32, 64 Gb; Computer a 1-2-3 TBs of spinnig disk or 128,256,512 Gb of SSD. Spinnning disks are slower but much cheaper than SSD.
* [Mother board](https://en.wikipedia.org/wiki/Motherboard)
* [Bus](https://en.wikipedia.org/wiki/Bus_(computing))
* [L1, L2, L3, ... CPU cache](https://en.wikipedia.org/wiki/CPU_cache)
* [GPU - Graphics Processing Unit](https://en.wikipedia.org/wiki/Graphics_processing_unit)
* [FPU - Floating Point Unit](https://en.wikipedia.org/wiki/Floating-point_unit)
* Input: keyboard, mouse, microphone, scanner, touchpad
* Output: Screen, printer
* [BIOS](https://en.wikipedia.org/wiki/BIOS)
* External connectors



## connectors
{id: connectors}

* [PS/2](https://en.wikipedia.org/wiki/PS/2_port)
* [Video Connectors](https://en.wikipedia.org/wiki/List_of_video_connectors): VGA, DVI, SDI, HDMI, DisplayPort, ...
* [USB 2,3](https://en.wikipedia.org/wiki/USB)
* [RJ45 - Ethernet](https://en.wikipedia.org/wiki/RJ45_(computers))
* [Wireless](https://en.wikipedia.org/wiki/Wi-Fi)
* [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)
* [Audio cables (3.5mm jack)](https://en.wikipedia.org/wiki/Phone_connector_(audio))
* [RJ11 - phone cable](https://en.wikipedia.org/wiki/RJ11)
* [Firewire](https://en.wikipedia.org/wiki/IEEE_1394)
* [Thunderbolt](https://en.wikipedia.org/wiki/Thunderbolt_(interface))



## bits and bytes
{id: bits}

```
base 10:        42
base 2:   00101010

 1 bit         0 or 1   (transistor)
 8 bit            256 = 1 byte
16 bit         65,536 = 64 kbyte
32 bit  4,294,967,296 = 4 Gb
64 bit  ~ 10 ** 20    = a lot
```

* [Binary numbers](https://en.wikipedia.org/wiki/Binary_number)
* [Transistor](https://en.wikipedia.org/wiki/Transistor)



## Y2K problem
{id: y2k-problem}
{i: Y2K}


Y2K problem (time represented as the last two digit of the year.
Instead of 1985 we wrote 85  saved space, looked clear.  You also knew that the year 86 was after the year 85 as 8 > 85.
It worked until 1999, but when 2000 came it was (supposed to be) represented as 00.
Suddenly tomorrow was before yesterday.

<a href="https://en.wikipedia.org/wiki/Year_2000_problem">Year 2000 problem</a>




## Year 2038 problem
{id: year-2038-problem}


* [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)
* 32 bit systems




## Incorrect floating point number representation
{id: floating-point-representation}




<a href="https://en.wikipedia.org/wiki/Floating-point_arithmetic">Floating point arithmetic</a>
e.g. in python:




```
1.2 - 1.0
0.19999999999999996
```



## Operating Systems
{id: operating-systems}


Desktop / Server


* [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
* [MacOS](https://en.wikipedia.org/wiki/MacOS) - Apple
* [Linux](https://en.wikipedia.org/wiki/Linux)
* [Unix](https://en.wikipedia.org/wiki/Unix) (Solaris, AIX, HP-UX)
* ...


Mobile


* [iOS](https://en.wikipedia.org/wiki/IOS) - Apple
* [Android](https://en.wikipedia.org/wiki/Android_(operating_system)) (Linux)
* [Windows Mobile](https://en.wikipedia.org/wiki/Windows_Mobile) (discontinued)
* ...


Embedded


* [VxWorks](https://en.wikipedia.org/wiki/VxWorks)



* Other Unix and Linux flavors
* Routers (and other networking equipment)
* [Cisco IOS](https://en.wikipedia.org/wiki/Cisco_IOS)
* What do weapon systems run?



## Programming paradigms
{id: programming-paradigms}

* imperative (global state, no functions)
* procedural - imperative (C, Bash)
* object oriented - imperative (Java, C#, C++)
* declarative (SQL)
* functional - declerative (Haskell)
* logic  - declerativ (Prolog)
* mathematical - declerative (Fortran)
* ...



Multi-paradigm: (e.g. Python, Perl)




## Different OOP systems
{id: different-oop-systems}

* Java - Hello World needs a class, but numbers and strings by themselves are not objects.
* Python - Even strings and numbers are objects, but you can just write a single line to print.

![](examples/hello_world.py)
![](examples/HelloWorld.java)


```
"abc".upper()
```


## Compiled vs Interpreted languages
{id: compiled-vs-interpreted-language}

* Compiled: C, C++
* Interpreted: Basic, Shell
* Python, Perl, ...?
* Java, C#, ...?



## Open Source
{id: open-source}

* What is Open Source
* Why does it matter?
* Cost
* Support
* Freedom
* License! GPL - BSD
* [Open Source Initiative](https://opensource.org/)



## Why create Open Source?
{id: why-create-open-source}



Why do people create and maintain them? Why do companies contribute to Open Source and why do they release under OS license?



* Fun, creative work
* I wrote this thing, but I don't want to sell it so why not?
* Get feedback
* Contribute
* Create a huge user-base a small fraction of it will pay money for extra services
* Undermine competitors




## Open Source languages
{id: language-tooling}

* Are there multiple compilers/interpreters for the language?
* Is the language definition free?
* Are the compilers/interpreters Open Source?
* IDEs ?
* Profilers?




## Version Control
{id: version-control}


* Fearless experimentations
* Fearless deletition
* Easier (smoother) collaboration
* History
* git, mercurial; subversion; cvs; rcs



## Software testing
{id: software-testing}

* Is it still working?
* Fearless changes
* Fearless upgrades
* Regression testing!
* Acceptance testing
* capacity, load, security etc.



## ASCII - Unicode
{id: ascii-unicode}


## Complexity
{id: complexity}

```
O(n)
O(n^2)
O(n log n)
```


## What is the Internet?
{id: what-is-the-internet}

* Computers
* Networking equipment (routers, bridges, ...)
* Cables
* Wireless transmitters
* Client-Server applications
* Web Servers, Database servers, ...
* ...



## What is the Cloud?
{id: what-is-the-cloud}

* Some other peoples computer.
* Server where you can rent some processing power.
* More sofisticated if you can rent the use of an application.
* Gmail
* Google docs
* Dropbox
* Google Cloud Service, Amazon Web Services (AWS), Microsoft Azure



## Software Development methods
{id: software-development-methods}

* Waterfall
* Agile?
* Scrum
* Kanban
* DevOps
* XP






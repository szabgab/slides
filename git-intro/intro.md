# DevOps Workshops: Git
{id: introduction-to-git}

## About us
{id: about-us}

* Yonit Gruber-Hazani
* Gabor Szabo
* DevOps Workshops http://devops-workshops.code-maven.com/

## About you
{id: about-you}

* Name
* Company
* What do you do
* Something interesting about you

## Version control Systems (VCS)
{id: vcs}

* Local Version Control Systems (LVCS)
* Centralized Version Control Systems (CVCSs)
* Distributed Version Control Systems (DVCS)

## Local Version Control Systems (LVCS)
{id: lvcs}

* Copy files, dated directories
* RCS, short for Revision Control System
* Save a series of patches
* Difficult to collaborate
* Branching is almost impossible

## Centralized Version Control Systems (CVCS)
{id: cvcs}

**Samples:**
* CVS, or Concurrent Versions System
* Apache Subversion (aka. SVN)
* Perforce
* Rational Clear-Case (IBM) (Configuration Management)

**Details:** 
* Central server holds everything (good/bad)
* Easier administration, better control
* Limited or no off-line work
* Single point of failure.
* Branching is easy in some cases (Subversion)
* Merging is still a pain

## Distributed Version Control Systems (DVCS)
{id: dvcs}

**Samples:**
* Git
* Mercurial (hg)
* GNU Bazaar (bzr)
* Darcs

**Details:** 
* Full copy of repository
* No central control (good/bad)
* No single point of failure
* Easy branching
* Easy merging
* Fast
* Allow off-line development

## Git Overview
{id: GitOverview}

* Snapshots of the objects (files) and not diffs. Using pointers eliminate duplications.
* Nearly every operation is local. (Off-line work)
* Integrity using SHA-1 hashes of the files. (40 character string of hexadecimal characters called "object name" or "SHA-1 id".)

## Git Installation
{id: GitInstallation}

On UNIX/Linux you use your package manger (apt-get, yum, etc...) or install from git-scm.
* yum install git-core
* apt-get install git-core
On Microsoft Windows install Git from msysgit (Git and not msysGit)
On Mac: Git OSX installer

## Which version do you have?
{id: version}

Windows

'''
c:\> git --version
git version 1.8.1.msysgit.1
'''

OSX

'''
$ git --version
git version 2.1.3
'''

## title
{id: title}


## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)
* [Slides of Gabor](https://code-maven.com/slides/git/)



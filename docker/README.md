* networking? (can I configure IP addresses)
* Set up a local repository
* Connect a a different (local) repository



* Show some interactive usage of Docker
* Commands on the command-line
* Show some cases with Dockerfile


- see the log files (/var/log/...) while the container is running, after the container has ended.
- In a production system, how do we collect (error) reports from containers?
- upload to server for production



Original hello-world is 1.84 kB
The one based onUbuntu is 121Mb

Distribute a web application (just flask)
Distribute a web application flask + nginx
Distribute a web application flask + nginx + MongoDB
Create an image with all the dependencies of a build and then reuse that image in every later stage. Rebuild the base image whenever the requirements file was changed.
docker pull
Create an image in the repository (from github)



That's really nice, but once we close the container we lose our changes.
When we run again we need to start from scratch.


$ docker run --rm mydocker

Use of uninitialized value $name in scalar chomp at /opt/greetings.pl line 7.
Use of uninitialized value $name in concatenation (.) or string at /opt/greetings.pl line 8.
What is your name? Hello , how are you today?


How to run develop Python programs using PyCharm or Vistual Studio Code on Windows and run the code inside a Docker container?


Examples in Ubuntu, Centos 7, and other distributions.

Add more stand-alone examples in other languages as well
Add example to use a persistent volume for the "database" (which can be either json file based or SQLite)
Each language can have its own chapter to make it easy to jump over the ones the student is not interested in.


Docker compose - two simple images that can see each other (ping ? ssh ?)
Docker one of them is a Redis server the other one is a Redis client?
(Same with all kinds of other services - MySQL, MariaDB, PostgreSQL, Pulsar)
The server must have persistent storage.
One of the is a server the other one is a client application.

Networking IPv4 IPv6 ?


docker build cache

docker builder prune


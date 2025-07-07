# What is Docker?



Docker is usually called a light-weight Virtual Server.

If you are familiar with VirtualBox or VMware you know they allow you to have
a full copy of any operating system running on top of your main operating system. You can even run multiple of these guest operating
systems on a single host operating system. There is full separation and you can install anything on each one of the guests.

However this is very resource intensive as each one of the guest Virtual Servers needs to run its own Operating system taking up a lot
of memory and using a lot of CPU cycles.

Docker also allows to run several guests on the same host, but if the host and the guest are the same type (e.g. both are Linux) then
the guest uses the same kernel as the host and thus requires a lot less additional resources. It has certain limitations such as one service
per each Docker, but these limitations are usually irrelevant in a real-life environment.

The action packaging a whole application inside a Virtual Server is called containerization. There are several solutions to do this, but
Docker got so popular that it is now the de-facto standard.


* A light-weight Virtual Server.

* De-facto standard for containerization.



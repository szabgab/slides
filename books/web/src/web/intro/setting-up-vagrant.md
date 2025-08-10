# Setting up Vagrant

* Install [Vagrant](https://www.vagrantup.com/)
* Install [VirtualBox](https://www.virtualbox.org/)
* vagrant init szabgab/pde
* Edit Vagrantfile adding the following lines:
* config.vm.network "forwarded_port", guest: 5000, host:5000
* config.vm.network "forwarded_port", guest: 3000, host:3000
* vagrant up  (first time this will download 800Mb file)
* [article](http://perlmaven.com/vagrant-perl-development-environment)
* vagrant ssh
* /vagrant is mapped to your directory on the host
* sudo apt-get install tree






## Just some thoughts on the topics that might be interesting to cover

-i inventoryfile.cfg
-m MODULE
-a ???
-f CONCURRENCY

ansible -i inventory.cfg all -m ping

Get information:
ansible -i inventory.cfg all -a hostname
    date
    uptime
    free

Automaticlly install the ssh public keys on a machine so subsequent commands won't need a password.

Do something based on the information we have retreived.
Store the information we have retreived.
Do some action based on the rc of the previous command.

Upgrade packages. - how can we know that the machine needs a reboot after the update?
Reboot server if necessary.

How to upgrade machines one-by-one? e.g. if we have 10 web servers we would not want to upgrade and reboot all of them at once.
Maybe we would like to do one and when it is up again then do the second and then the third etc.

Change the hostname of the server.
Install Nginx / Apache.

Configure Nginx:
   add / update configuration file
   restart server

Install Python packages (e.g. Flask) and run a stand-alone Flask application.
Install uwsgi and configure it to run the flask application.

Install a cron-job to user foo
Install a cron-job to user root

ansible -i inventory.cfg all -a "perl -mPath::Tiny -E 'say $Path::Tiny::VERSION'"

Install Munin (or other monitoring agent) on the hosts.

See a list of tasks that one would normally do using Ansible.


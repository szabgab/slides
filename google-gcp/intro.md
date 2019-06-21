# Google Cloud Platform
{id: index}

## Self intro
{id: self-intro}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

* [Workshops](https://workshops.code-maven.com/)
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)

## Registration
{id: registration}

* [Google Cloud](https://cloud.google.com/)
* Credit Card
* Some free usage

I strongly recommend you use your own private Google account for this and you create your own Google Cloud account
and you don't use your employers account. If for no other reason, then because in that corporate account you might
have certain limitations that will make it impossible to do some of the exercises.

Google provides you with some credit to experiment with their services without actually paying money, but they still
require a valid credit card to create the account. If you don't want to provide that then I am afraid you won't
be able to try this.

## Remove services!
{id: remove-services}

* At the end of the session don't forget to stop and even to remove services!
* Otherwise they might eat your credit.

* Stop and even remove instances.
* Remove public IP address registations.
* Remove snapshots.
* Remove images.
* Remove instance groups.

## Menu of the console
{id: menu-of-the-console}

* [Console](https://console.cloud.google.com/)
* "Pin" the "[Compute Engine](https://console.cloud.google.com/compute/instances)" to make it easier to access.

Some other insteresting entries

* IAM - Identity Access Management, where you can allow other people (and devices) to have certain rights in your account.
* Compute Engine - Virtual Machines (we'll start with this)
* Kubernetes - to run Docker images
* Storage - various types of managed databases and filesystems

## Create VM Instance
{id: create-vm-instance}

* Name (fixed)
* Region, Zone (fixed)

* Machine Type
* Price
* Boot disk / OS image (fixed)

There are only very few options that are "fixed" once you create the instance. Most of them can be changed later.
Some can be changed while the instance is running, others require it to be shut down and restarted.

Look at the prices. They charge by the second, so you can turn on and off instances without using a lot of the credit
you have.

## VM Instance Example
{id: vm-instance-example}

* Launch the smallest possible instance (micro)

## Access VM in browser
{id: access-vm-in-browser}

* SSH - Open in browser window


## Install packages - http
{id: install-packages}

* Check htop and install it
* curl http://localhost/
* Install nginx and try curl again

```
sudo apt-get install htop
sudo apt-get install nginx
curl http://localhost/
```
* Allow http traffic (while the instance is running)

## Stop instances
{id: stop-instance}

* Stop instance will take more than 1:30 minutes
* Refresh

## Exercise 1
{id: exercise-1}

* Sign up to Google Cloud.
* Create a micro instance with your favorite Linux distribution.
* Access it using the web-based SSH client.
* Try curl on localhost. It will fail as there is no web server.
* Install nginx.
* Try curl again.
* Change the default web page. (See /etc/nginx )
* Install your favorite server or command line tool.
* Shut down the instance.


## Google Cloud SDK - command line tools
{id: cloud-sdk}

* [Google Cloud SDK](https://cloud.google.com/sdk/)
* [gcloud](https://cloud.google.com/sdk/gcloud/)
* [gsutil](https://cloud.google.com/storage/docs/gsutil)

```
gcloud init
```

## List instances
{id: list-instances}

```
gcloud compute instances list
```

## Access instance using gcloud
{id: access-instance-using-gcloud}

```
gcloud compute ssh NAME
```

## Snapshots
{id: snapshots}

* [Compute Engine / Snapshots](https://console.cloud.google.com/compute/snapshots).
* Create a snapshot based on the disk of VM (which is running).

* Scheduled snapshot creation.


## Extra disk
{id: extra-disk}


* Compute Engine - VM Instances
* Edit the VM where we would like to attach the disk "Additional disks"
* "Attach existing disk"

```
$ sudo lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda      8:0    0  10G  0 disk
└─sda1   8:1    0  10G  0 part /
sdb      8:16   0  20G  0 disk
```

```
sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
```

Mount disk

```
sudo mkdir /mnt/data
sudo mount -o discard,defaults /dev/sdb /mnt/data
df -h
```

Add a file

```
sudo chmod a+w /mnt/data
touch /mnt/data/YOURNAME
```


```
sudo blkid /dev/sdb
/dev/sdb: UUID="51b624c7-81ad-4c17-849c-142908acff50" TYPE="ext4"
```

Edit /etc/fstab and add:

```
UUID=51b624c7-81ad-4c17-849c-142908acff50 /mnt/data ext4 discard,defaults,nofail 0 2
```

then you should be able to

```
sudo mount /mnt/data
sudo umount /mnt/data
```

* [Compute Engine - Disks](https://console.cloud.google.com/compute/disks)
* Read: [Add persistant disk](https://cloud.google.com/compute/docs/disks/add-persistent-disk)

## Delete instance
{id: delete-instance}

## Create instance based on a snapshot
{id: create-instance-based-on-snapshot}

* Create instance
* Boot disk - Change - Snapshots

## Exercise 2
{id: exercise-2}

* Install and configure Google Cloud SDK.
* Access the instance using gcloud.
* Create an instance using on the console or using [gcloud compute instances create](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create)
* Create a file on the instance (just to see it remained on the new instance).
* Create a snapshot.
* Create a new instance based on the snapshot.
* Add a new disk to the instance.

## Meta-data
{id: metadata}

* Some are provided by Google.
* Some can be set by us either project-wide or per instance.

## Access Metadata
{id: access-metadata}

* On the instance:

```
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/hostname
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/name
```

## Metadata - key-value pairs
{id: metadata-key-value-pairs}

* Compute Engine - Metadata - Metadata - Edit
* Add 'organization' = 'Some value'

```
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/project/attributes/organization
```

## Metadata on the instance
{id: metadata-on-the-instance}

* Compute Engine - VM instances - (instance) - edit
* Custom metadata
* Set 'hello' : 'world'

```
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/hello
```

## Metadata - ssh keys
{id: metadata-ssh-keys}

* If you don't have one yet, create an shh key on your computer
* [Compute Engine - Metadata - SSH Keys](https://console.cloud.google.com/compute/metadata/sshKeys) - Edit
* Paste the public key there

* Try to ssh to the instance from a regular SSH client.

```
alias xscp='scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
alias xssh='ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
```

## Labels
{id: labels}

* Labels allow us to organize resources.
* Can help us allocate expenses to project/clients/etc.


## Static or Fixed IP Address
{id: fixed-ip-address}

* Set up fixed IP address.
* [VPC Network - External IP Addresses](https://console.cloud.google.com/networking/addresses/list).
* Reserve static address.

* [Reserve Static IP address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address)

## Exercise 3
{id: exercise-3}

* Make sure you have a server running!.
* If you don't have it yet, create an ssh key on your local computer.
* (Windows users can use the git-bash terminal.)
* Add the public key to the project-wise Meta-Data
* Try to ssh to the remote servers public IP using the command-line ssh client.
* Add a label to the instance.
* Record the current public IP address.
* Shut down the instance.
* Start it again, observe the change in public IP address.
* Create a fixed IP address.
* Shut down/start again.
* Remove the fixed IP address (as that costs money when unused).


## Create preemptible instance
{id: create-preemptible-instance}

* Similar to spot instance in Amazon.
* Can be tuned off any time.
* Max life-span is 24 hours.
* ~ 20% of the cost.

## Instance Group
{id: instance-group}

* Automatic scaling.

* Create and Image
* Create an Instance template
* Create an Instance group

## Create Image
{id: create-image}

* Create an instance.
* Install `htop`.
* Copy the following file.

![load](load.py)

* Shut down the instance.
* [Create an image](https://console.cloud.google.com/compute/images) based on the disk of the instance.
* Start an instance based on the image, verify it and then destroy it.

## Create Instance template
{id: create-instance-template}

* [Create Instance Template](https://console.cloud.google.com/compute/instanceTemplates/list)

## Create Instance Group
{id: create-instance-group}

* [Create Instance Group](https://console.cloud.google.com/compute/instanceGroups/list)

## Exercise 4
{id: exercise-4}

* Create an instance with the loader script.
* Create an image.
* Cerate a template for the smallest instance possible.
* Create an instance group with 1-10 nodes.
* There should be one instance running.
* Connect to it in two ssh sessions, one with htop, the other runs the load generator.
* See how increasing load make the system increase the number of running instances.

* Don't forget to destroy the instance group!

## QA
{id: qa}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

* [Workshops](https://workshops.code-maven.com/)
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)



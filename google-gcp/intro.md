# Google Cloud Platform
{id: index}

## Self intro
{id: self-intro}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

* [Workshops](https://workshops.code-maven.com/)
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)


## Registration
{id: registration}

* Credit Card
* Some free usage


## Menu of the console
{id: menu-of-the-console}

* "Pin" the "Compute Engine" to make it easier to access.

## Create VM Instance
{id: create-vm-instance}

* Name (fixed)
* Region, Zone (fixed)

* Machine Type
* Price
* Boot disk (OS image)


## VM Instance Example
{id: vm-instance-example}

* Launch the smallest possible instance (micro)

## Access VM in browser
{id: access-vm-in-browser}

* SSH - Open in browser window


## Google Cloud SDK
{id: cloud-sdk}

* [Google Cloud SDK](https://cloud.google.com/sdk/)
* [gcloud](https://cloud.google.com/sdk/gcloud/)
* [gsutil](https://cloud.google.com/storage/docs/gsutil)

```
gcloud init
```

## Access instance using gcloud
{id: access-instance-using-gcloud}

```
gcloud compute ssh NAME
```

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

* Sign up to Google Cloud
* Create a micro instance with your favorite Linux distribution)
* Access it using the web-based SSH client
* Install and configure Google Cloud SDK
* Access the instance using gcloud.
* Try curl on localhost
* Install nginx
* try curl again
* change the default web page
* shut down the instance.


## Snapshots
{id: snapshots}

* Compute Engine / Snapshots
* Create a snapshot based on the disk of VM (which is running)

* Scheduled snapshot creation


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


* Compute Engine - Disks
* [Add persistant disk](https://cloud.google.com/compute/docs/disks/add-persistent-disk)


## Delete instance
{id: delete-instance}

## Create instance based on a snapshot
{id: create-instance-based-on-snapshot}

* Create instance
* Boot disk - Change - Snapshots

## Access Metadata
{id: access-metadata}

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
* Compute Engine - Metadata - SSH Keys - Edit
* Paste the public key there

* Try to ssh to the instance from a regular SSH client.

## Labels
{id: labels}

* Labels allow us to organize resources
* Can help us allocate expenses to project/clients/etc.


## Static of Fixed IP Address
{id: fixed-ip-address}

* Set up fixed IP address
* VPC Network - External IP Addresses
* Reserve static address

* [Reserve Static IP address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address)

## Create preemptible instance
{id: create-preemptible-instance}

* Similar to spot instance in Amazon
* Can be tuned off any time
* Max life-span is 24 hours

## Create Image
{id: create-image}

* Create an instance
* Install `htop`
* Copy the following file

![load](load.py)

* Shut down the instance
* Create an image based on the disk of the instance

## Create Instance template
{id: create-instance-template}

## Create Instance Group
{id: create-instance-group}




## QA
{id: qa}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

* [Workshops](https://workshops.code-maven.com/)
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)



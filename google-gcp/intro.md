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


## Install gcloud
{id: install-gcloud}


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

## Snapshots
{id: snapshots}

* Compute Engin / Snapshots
* Create a snapshot based on the disk of VM (which is off)


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


## Fixed IP Address
{id: fixed-ip-address}

* Set up fixed IP address


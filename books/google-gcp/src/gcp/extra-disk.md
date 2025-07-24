# Extra disk


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



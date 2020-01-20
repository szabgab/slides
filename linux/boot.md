# Boot
{id: boot}

## Boot stages
{id: boot-stages}

1. BIOS - Basic Input/Output System of the hardware
1. boot loader
1. The Linux kernel.
1. The init process.



## BIOS
{id: bios}

* Hardware specific.
* Checks hardware extensions.
* Configurable: (e.g. the boot device)
* F12 ???
* Executes the code in the Master Boot Record (MBR) of the selected device.



## Boot loader
{id: boot-loader}

* Located in the Master Boot Record (MBR) of the HD/CD/disk on key.
* LILO - Linux Loader (old)
* GRUB - Grand Universal Bootloader (modern)



## Grub
{id: grub}

* /etc/grub.conf
* Allows the user to select which kernel to load or which options to pass
* Single user mode!



## init
{id: init}

* /sbin/init
* initrd



## Multiple OS-es
{id: multiple-os-es}

* Dual boot.
* Host/Guest using Virtualbox or other simple virtulatization
* virtualization - slicing of the resources.






# Create Image

* Create an instance.
* Install `htop`.
* Copy the following file.

{% embed include file="src/examples/gcp/load.py" %}

* Shut down the instance.
* [Create an image](https://console.cloud.google.com/compute/images) based on the disk of the instance.
* Start an instance based on the image, verify it and then destroy it.



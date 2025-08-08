# Solution: chmod

* Create a second user **sudo adduser foo**
* Create the file and make it  executable by owner and by group **chmod ug+x hello.sh**
* Create a new group:   **sudo groupadd exe**
* Add my user (vagrant) to this group: **sudo usermod -a -G exe vagrant**
* Add the second user (foo) to the group: **sudo usermod -a -G exe foo**
* Change the group of the file to be the new common group: **sudo chgrp exe hello.sh**



# Jenkins master/agent


* Create another VPS and ssh to it
* Create user bob:   adduser bob
* Create ssh public key of the Jenkins user **ssh-keygen** copy **/var/lib/jenkins/.ssh/id_rsa.pub** from the Jenkins server to /home/bob/.ssh/authorized_keys on the machine that will be used as an agent and then chown -R bob.bob /home/bob/.ssh/
* Verify that user jenkins can ssh to user bob on the agent machine without supplying any password.
* If No entry currently exists in the Known Hosts file for this host: Run this as user jenkins on the master:
* **ssh-keyscan -H 107.170.12.117 >> ~/.ssh/known_hosts**



* Remote home directory: /home/bob
* Launch method: via SSH
* SSH Username with private key
* Username: bob
* Private Key: From the Jenkins master ~/.ssh


```
Manage Jenkins
    Manage nodes
       New node, Node name: s1   - Permanent Agent
```



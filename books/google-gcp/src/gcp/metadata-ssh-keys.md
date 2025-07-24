# Metadata - ssh keys

* If you don't have one yet, create an shh key on your computer
* [Compute Engine - Metadata - SSH Keys](https://console.cloud.google.com/compute/metadata/sshKeys) - Edit
* Paste the public key there

* Try to ssh to the instance from a regular SSH client.

```
alias xscp='scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
alias xssh='ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
```



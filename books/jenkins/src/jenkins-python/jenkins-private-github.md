# Jenkins: Private GitHub repository

* Create private/public keypair: su - jenkins; ssh-keygen; ENTER * 3
* `cat .ssh/id_rsa.pub` and copy paste it the GitHub repo Settings / Deploy keys
* Try cloning the private repo still as use jenkins: **git clone git@github.com:szabgab/python-test-private.git**
* In the Jenkins GUI setup separate job called **python-test-private** where the Git / Repositories is git@github.com:szabgab/python-test-private.git
* Add Jenkins credentials: "SSH Username with private key", Username: git, Private Key: From the Jenkins master ~/.ssh




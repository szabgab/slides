# NodeJS Installation Linux


By the time you are reading this, there might have a newer LTS version already.

```
export NODEJS=v14.15.1
wget https://nodejs.org/dist/$NODEJS/node-$NODEJS-linux-x64.tar.xz
tar xf node-$NODEJS-linux-x64.tar.xz
sudo mv node-$NODEJS-linux-x64/ /opt
sudo chown -R root.root /opt/node-$NODEJS-linux-x64/
sudo ln -s /opt/node-$NODEJS-linux-x64 /opt/node
```

Add it to the PATH:

```
echo "export PATH=\$PATH:/opt/node/bin" >> ~/.bashrc
```



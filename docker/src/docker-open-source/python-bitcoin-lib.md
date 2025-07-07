# Python Bitcoinlib

* [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)

Steps to run tests on a docker container:

```
git clone https://github.com/petertodd/python-bitcoinlib.git
cd python-bitcoinlib
docker run -it --name python-bitcoinlib -w /opt -v$(pwd):/opt python:3.11 bash
python3 -m unittest discover
```



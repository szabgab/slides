# Travis-CI on OSX


Travis allows the use of Mac OSX for your tests. In order to do that you need to include `os: osx` in the configuration file. (`os` defaults to `linux`).

Setting `dist: osx` is a mistake. It will mean no build is triggered. Unfortunately I did not even see an error message from Travis telling me that my configuration is incorrect.


* Setting `os: osx`

* This image has different default tools. For example it does not have docker, nor lsb_release.

{% embed include file="src/examples/minimal-osx/.travis.yml" %}

{% embed include file="src/examples/minimal-osx/run.sh)

[Build environments](https://docs.travis-ci.com/user/reference/overview/)



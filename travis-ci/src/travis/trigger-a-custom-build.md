# Trigger a custom build


* Can be good for experimentation with Travis without he need to make commits to the repository

* More Options / Trigger Build
* Set a commit message
* copy (or type in) the content of a YAML file, it will be merged into the regular .travis.yml
* (e.g. add more versions of the language)


Setting

```
TRAVIS_EVENT_TYPE=api
```

instead of the usual `push`.

* [Environment Variables](https://docs.travis-ci.com/user/environment-variables/)



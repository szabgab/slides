# Examples

* [The examples are on GitHub](https://github.com/szabgab/slides)
* You can download them and unzip them or you can clone them using

```
git clone https://github.com/szabgab/slides.git
```

```
'slides'... fatal: unable to access 'https://github.com/szabgab/slides.git/':
SSL certificate problem: self signed certificate in certificate chain
```

Sometimes people get an error:

The soulution is then to do the following: (on Windows)

```
set GIT_SSL_NO_VERIFY=true
git clone https://github.com/szabgab/slides.git
```


Later, after I update the slides you can also update your local copy of the files by running

```
cd slides
git pull
```



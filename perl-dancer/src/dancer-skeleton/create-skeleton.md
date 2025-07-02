# Create skeleton with dancer2 -a


```
dancer2 -a App::Skeleton
```

Creates the following structure


```
App-Skeleton/
├── bin
│   └── app.psgi
├── config.yml
├── cpanfile
├── environments
│   ├── development.yml
│   └── production.yml
├── lib
│   └── App
│       └── Skeleton.pm
├── Makefile.PL
├── MANIFEST
├── MANIFEST.SKIP
├── public
│   ├── 404.html
│   ├── 500.html
│   ├── css
│   │   ├── error.css
│   │   └── style.css
│   ├── dispatch.cgi
│   ├── dispatch.fcgi
│   ├── favicon.ico
│   ├── images
│   │   ├── perldancer-bg.jpg
│   │   └── perldancer.jpg
│   └── javascripts
│       └── jquery.js
├── t
│   ├── 001_base.t
│   └── 002_index_route.t
└── views
    ├── index.tt
    └── layouts
        └── main.tt

11 directories, 23 files
```

It also tells you to

```
cd App-Skeleton
plackup bin/app.psgi
```

To run the tests:

```
prove -l
```




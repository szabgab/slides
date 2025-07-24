# Installing modules on ActivePerl

```
C:> ppm
ppm> install Name-Of-Module
```

in case it returns a list of modules, pick up the correct number:

```
ppm> install 3
```

There are additional sites with ppm repositories once can find on Kobes Search

Add the repository to ppm and install modules from that place as well:

```
ppm> rep add uwin http://theoryx5.uwinnipeg.ca/ppms/
ppm> install IO-Socket-SSL 
```

in ActiveState 5.6.x 

```
ppm> set rep name URL
```

In case the computer is behind a company proxy you can configure 
the http_proxy environment variable and ppm will use the proxy:

```
set http_proxy=http://proxy.company.com:8080
```




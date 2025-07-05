# Install a package


Let's try again:

```
$ ansible virtualhosts -m apt -a "name=nginx state=present" -b

ubuntu-2 | SUCCESS => {
    "cache_update_time": 1521409853,
    "cache_updated": false,
    "changed": true,
    "stderr": "",
    "stderr_lines": [],
    "stdout": "Reading package lists...\nBuilding dependency tree...\nReading state information...\n
              The following additional packages will be installed:\n  fontconfig-config fonts-dejavu-core
              libfontconfig1 libgd3 libjbig0\n  libjpeg-turbo8 libjpeg8 libnginx-mod-http-geoip\n
              libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter\n  libnginx-mod-mail
              libnginx-mod-stream libtiff5 libwebp6 libxpm4 nginx-common\n  nginx-core\nSuggested packages:\n
              libgd-tools fcgiwrap nginx-doc ssl-cert\nThe following NEW packages will be installed:\n
              fontconfig-config fonts-dejavu-core libfontconfig1 libgd3 libjbig0\n  libjpeg-turbo8
              libjpeg8 libnginx-mod-http-geoip\n  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter\n
              libnginx-mod-mail libnginx-mod-stream libtiff5 libwebp6 libxpm4 nginx\n  nginx-common nginx-core\n
              0 upgraded, 18 newly installed
```

Let's check from one of the servers:

```
yonit@ubuntu-2:~$ service nginx status

   nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2018-03-19 00:15:24 IST; 1min 1s ago
     Docs: man:nginx(8)
```

You can try to access it:

```
$ curl http://ubuntu-1
```



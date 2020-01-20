# Backend
{id: mobile-backend}

## Start with Dancer
{id: start-with-dancer}
{i: dancer}

* **dancer -a App::Name**
* cd App-Name
* perl bin/app.pl
* browse to http://localhost:3000
* edit views\index.tt
* edit App-Name/lib/App/Name.pm


{aside}

The dancer -a command will create the App-Name subdirectory with several files.
Most importantly for us, the App-Name/lib/App/Name.pm
{/aside}


## Module
{id: backend-module}
![](examples/backend/MEB.pm)


## Front-end server
{id: front-end-server}
![](examples/app.psgi)


## Same origin policy
{id: same-origin-policy}


Turn off same-origin-policy in Chrome
<a href="http://stackoverflow.com/questions/3102819/chrome-disable-same-origin-policy"></a>



```
chromium-browser --disable-web-security
google-chrome --disable-web-security

Windows: The target in the short-cut:
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
   --disable-web-security

Mac:
open /Applications/Google\ Chrome.app/ --args --disable-web-security
```


In Firefox: <a href="https://addons.mozilla.org/en-us/firefox/addon/forcecors/"></a>






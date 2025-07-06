# Get request headers using Firefox


Just to compare, when I visited [this url](https://httpbin.org/headers) using [Firefox](https://www.mozilla.org/en-US/firefox/new/), my default browser I get the
following results:

```
{
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Host": "httpbin.org",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "X-Amzn-Trace-Id": "Root=1-6394b5d7-395b7a2a377ea2df7dd4dbe8"
  }
}
```

Here the User-Agent is more detailed.


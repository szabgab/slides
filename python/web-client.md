# Web client - web scraping
{id: python-web}

## get HTML page using urllib
{id: urllib}
{i: urllib}

{aside}
urllib is a rather low level library. It comes standard with Python.
{/aside}

* [urllib](https://docs.python.org/library/urllib.html)

![](examples/web-client/with_urllib.py)

## Download image using urllib
{id: urllib-download}

{aside}
Usually you will want to save the downloaded image to the local disk.
{/aside}

![](examples/web-client/download_image_with_urllib.py)

## get HTML page using requests
{id: requests-get}
{i: requests}

{aside}
requests is the de-facto standard in Python for dealing with web pages as a web client.
{/aside}

* [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [Python requests](http://docs.python-requests.org/)

![](examples/web-client/requests_get.py)

## Download image using requests
{id: dowload-image-using-requests}

![](examples/web-client/download_image_with_requests.py)

## Download image as a stream using requests
{id: dowload-image-as-a-stream-using-requests}

{aside}
OK, this is not such a good example for streaming.
{/aside}

![](examples/web-client/download_image_with_requests_in_stream.py)

## Download zip file using requests
{id: download-zip-file}

![](examples/web-client/download_zip_file.py)

## Extract zip file
{id: extract-zip-file}
{i: zipfile}
{i: unzip}
{i: zip}

{aside}
This is unrelated, but once you have downloaded a zip file you will need to be able to extract its content.
This example shows how to unzip a file already on your disk.
{/aside}

* [zipfile](https://docs.python.org/library/zipfile.html)

![](examples/web-client/unzip_file.py)


## Beautiful Soup to parse HTML
{id: beautiful-soup}
{i: bs4}
{i: BeautifulSoup}

* [Beautiful soup](https://beautiful-soup-4.readthedocs.io/)

![](examples/web-client/parse_html.py)

## requests - JSON - API
{id: requests-and-json}

{aside}
Downloading HTML pages and parsing them to extract data can be a lot of fun, but it is also very unstable.
Page layouts will change. The code will break easily. In many cases there is a better way. Use the API provided by the site.
{/aside}

## httpbin.org
{id: httpbin-org}

* [httpbin.org](https://httpbin.org) a website to practice various URL requests
* [source code](https://github.com/Runscope/httpbin) of httpbin.

## requests get from httpbin - JSON
{id: requests-get-httpbin}

![](examples/web-client/httpbin_get.py)

## requests get IP from httpbin - JSON
{id: requests-get-json}

![](examples/web-client/requests_get_json.py)


## requests get JSON User-Agent
{id: requests-get-json-ua}

{aside}
When our browser sends a requests it identifies itself.
{/aside}

* [See your User-Agent](https://httpbin.org/user-agent)

![](examples/web-client/requests_get_json_ua.py)


## requests change User-Agent
{id: requests-change-ua}

![](examples/web-client/requests_get_json_ua_changed.py)


## requests get header
{id: requests-get-headers}

{aside}
httpbin makes it easy to see what kind of headers your browser sends. Not only the User Agent
{/aside}

* [headers](https://httpbin.org/headers)

![](examples/web-client/requests_get_headers.py)

## requests change header
{id: requests-change-headers}

{aside}
The requests module too sends a set of default headers, but you can tell it to send other fields and values as well.
This examples shows how to 
{/aside}

![](examples/web-client/requests_change_headers.py)


## requests post
{id: requests-post}

{aside}
We can also send POST requests to an address with any payload (content).
{/aside}

![](examples/web-client/requests_post.py)

## Interactive Requests
{id: interactive-requests}

![](examples/web-client/interactive_requests.py)


## Tweet
{id: tweet}

* [Twitter developer](https://developer.twitter.com/)
* [Twitter API](https://developer.twitter.com/en/support/twitter-api)

![](examples/web-client/tweet.py)

## bit.ly
{id: bitly}

* [bit.ly API](https://dev.bitly.com/api-reference/)

![](examples/web-client/bitly.py)


## API config file
{id: api-config-file}

![](examples/web-client/api.cfg)

https://www.accuweather.com/
https://www.meteomatics.com/


## Exercise: Combine web server and client
{id: exercise-web}

Write a web application that can get a site and a text as input (e.g. http://cnn.com  and 'Korea')
check if on the given site the word appears or not?


Extended version: Only get the URL as the input and create statistics, which are the most
frequent words on the given page.



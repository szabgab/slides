# HTML5
{id: mobile-html5}

## HTML5 Features
{id: html5-features}

{aside}

HTML5 is not one big set of feature, but instead it is a set of individual feature. Each
browser supporting a subset of it. Which just makes it more difficult to build using it...

HTML5 adds new tags *and* corresponding API in the DOM (Document Object Model).
{/aside}

* Canvas - to draw using JavaScript.
* Video - to play video without extra plugins.
* Local Storage - to hold a lot of data on the client.
* Web Workers - threadding for your JavaScript in the browser.
* Offline web application - to download web elements and store locally.
* Geolocation - to know where the client is.
* Input types
* Placeholder text in input fields



## Input types
{id: html5-input-types}

* search for searchboxes
* number for spinboxes
* range for sliders
* color for color pickers
* tel for phone numbers
* url for web addresses
* email for email addresses
* date for calendar date picks
* month for months
* week for weeks
* time for timestamps
* datetime for precise, absolute date and timestamps
* datetime-local for local dates and times


Placeholder


* input.placeholder



## Check for availability
{id: check-for-avilability}
{i: Modernizr}


Modernizr.inputtypes.TYPE where TYPE is one of the names mentioned previously.




[modernizr](http://modernizr.com/) is a JavaScript library that detects HTML5 and CSS3 features in the user's browser.


![](examples/html_modernizr.html)


See also [detect](http://diveintohtml5.info/detect.html)


## HTML 5 as recognized by Modernizr
{id: html5-features-by-modernizr}

Modernizr.


* canvas
* canvastext
* video
* video.webm
* video.ogg
* video.h264
* localstorage
* webworkers
* applicationcache
* geolocation
* inputtypes.date
* inputtypes....



## HTML5 features
{id: html5-features-example}
![](examples/html5.html)


## Geolocation
{id: geolocation}

How to determine the location:


* based on IP address
* wifi connection
* cell tower information
* GPS hardware



## New semantic elements
{id: new-semantic-elements}

All wrapped in &lt; and &gt; signs.


* section
* nav
* article
* aside
* hgroup
* header
* footer
* time
* mark

See also [semantics](http://diveintohtml5.info/semantics.html)


## HTML5 Local storage
{id: local-storage}

Several names referring to the same thing:


* Local Storage
* Web Storage
* DOM Storage
* HTML5 Storage


A simple set of key/value pairs.



## Storage as strings
{id: storage-as-strings}
{i: localStorage.setItem}
{i: localStorage.getItem}
{i: localStorage.removeItem}

Values are stored as strings so on retrieval you'll need to use functions

![](examples/store/string.html)


## Store and stringify
{id: store}
{i: stringify}
{i: JSON}
![](examples/store/store.html)
![](examples/store/store.js)





# HTML and CSS
{id: html-and-css}

## Emulate devices
{id: view-page-as-on-device}


In Chrome show the page as if it was on a device.



* Right click, inspect element, select device



## Browserstack screenshots
{id: browserstack}

* [Browserstack screenshots](https://www.browserstack.com/screenshots)



## Mobile or Responsive?
{id: mobile-or-responsive}

* No mobile support
* [Perl.org](http://perl.org/) the 
* Mobile subdomain - Two types of web sites:  regular and mobile
* [Ynet](http://ynet.co.il/)
* [mobile Ynet](http://m.ynet.co.il/)
* Responsive Design.  Examples:
* [YAPC::NA](http://www.yapcna.org/yn2016/)
* [MetaCPAN](https://metacpan.org/pod/Mojolicious)
* [Media Queries](http://mediaqueri.es/)
* [Python.org](http://python.org/)



## HTML elements
{id: html-elements}

`<p> </p>`

* p
* h1, h2, ... h6
* div
* ul, ol, li
* table - tr, th, td
* span

* html - head, body
* hed - title

Attributes:

* a href
* img src

* id
* class


## Bare HTML
{id: bare-html}

![](examples/html/bare_html.html)


## HTML and CSS
{id: html-css}
![](examples/html/html_css.html)


## Viewport and Media Query for body
{id: viewport-and-media-query-body}
{i: viewport}
{i: @media}
{i: screen}
{i: min-width}
{i: max-width}
![](examples/html/viewport_media_body.html)


## Viewport and Media Query
{id: viewport-and-media-query}
![](examples/html/viewport_media.html)


## Pixels (px), em, rem
{id: units}
{i: px}
{i: em}
{i: rem}

* px
* em
* rem



## Units: px (pixels)
{id: units-pixels}

Fixed size on a given screen, If used with Media Queries we have to manually calculate and update each value.

![](examples/html/page_px.html)
![](examples/html/page_px.css)


## Units: em (The size of Letter M)
{id: units-em}

Relative to the font-size of the element.

![](examples/html/page_em.html)
![](examples/html/page_em.css)


The problem will be if we add another css directive insied the 'p' directive. eg. 'border 1em solid red'.
In this case the 1em will be relative to the font size of the 'p' element and not the font-size of the 'html'
element. So within the same 'p' element '2emp' of the 'font-size' and '1em' of the 'border' will be equal.




## Units: rem (root em)
{id: units-rem}

Relative to the font-size of the html element.

![](examples/html/page_rem.html)
![](examples/html/page_rem.css)


## Viewport width and height
{id: viewport-width-and-height}
{i: vw}
{i: vh}

* vw = viewport width  100vw  is 100% of the viewport
* vh = viewport height 100vh  is 100% of the viewport



## Exercise: Responsive HTML
{id: exercise-responsive-html}


Given an HTML page as in this example with a bunch of images,
resize the images to be small and of the same size when the screen is small,
but larger as the screen grows. Have at least 2 breaking points.


![](examples/html/thumbnails.html)





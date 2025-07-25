# SVG loaded in an img tag

In many cases it is probbably better to separate the SVG content from the HTML itself with all the usual pro and contra reasons.

Pro:
* separating the SVG file allows the developer to vide and edit it separately
* browsers can cache the svg image and this if the same image is reused on multiple page the browser does not need to load the data several times.

Contra:
* Browsers need to make a separate request to load each SVG file.


Move the SVG part to a separate file with `.svg` extension:

{% embed include file="src/examples/load-svg-via-img-tag.svg" %}

In the HTML document refer to the file via an `img` tag:

{% embed include file="src/examples/load-svg-via-img-tag.html" %}


The page is rendered like this:

![](/examples/svg-loaded-via-html-tag.png)

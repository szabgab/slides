# Bootstrap
{id: bootstrap}

## Start with Bootstrap
{id: start-with-bootstrap}

1. [Download Bootstrap](http://getbootstrap.com/).
1. Unzip the file.
1. ... or use the CDN
1. Create HTML file using the resources provied by Bootstrap.
1. ... or a simple skeleton.




## HTML5 Skeleton
{id: html5-skeleton}
{i: DOCTYPE}
{i: viewport}
![](examples/bootstrap/html5-skeleton.html)


## Bootstrap Skeleton
{id: bootstrap-skeleton}
![](examples/bootstrap/bootstrap-skeleton.html)



## Bootstrap HTML Tags
{id: bootstrap-html-tags}
{i: h1}
{i: mark}
{i: del}
{i: s}
{i: ins}
{i: u}
{i: small}
{i: em}
{i: strong}
![](examples/bootstrap/bootstrap-html-tags.html)



## Bootstrap Grid
{id: bootstrap-grid}

Bootstrap has two grids:


* Responsive
* Fluid


They both help us to divide the screen into 12 equal sized columns, or several blocks of columns that add up to 12.



## Fluid Container, rows and columns
{id: fluid-container}
{i: link}
{i: container}
{i: container-fluid}
{i: row}
{i: col-md-1}

* container will leave a large margin
* container-fluid is full-page
* rows need to be divided into 12 columns (or fewer that add up to 12)
* col-md-1, col-md-2 ..

![](examples/bootstrap/fluid-container.html)


## Buttons
{id: buttons}

* btn
* Size: btn-lg btn-sm btn-xs
* Color: btn-default btn-primary btn-success btn-info btn-warning btn-danger btn-link
* Mix the two

![](examples/bootstrap/buttons.html)


## Glyphicons
{id: glyphicons}

* Provided by [Glyphicons](http://glyphicons.com/)
* In Bootstrap 3 they are in the fonts/ director
* [Embedded OpenType (EOT)](https://en.wikipedia.org/wiki/Embedded_OpenType)
* [Scalable Vector Graphics (SVG)](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics)
* [Web Open Font Format (WOFF and WOFF2)](https://en.wikipedia.org/wiki/Web_Open_Font_Format)
* [TrueType Font (TTF)](https://en.wikipedia.org/wiki/TrueType)
* We need eot
* [Available Glyphicons](http://getbootstrap.com/components/#glyphicons)
* glyphicon
* glyphicon-search ...
* aria-label and aria-hidden are important for screen-readers.
* (The first is read out, the second can hide elements useless to screen-readers.)

![](examples/bootstrap/glyphicons.html)


## Menu or navigation bar
{id: navigation-bar}

* The 'Toggle navigation' is the button that is show on mobile devices opening the menu. (JavaScript required)
* For the drop-down to work we need to include js/bootstrap.min.js that requires JQuery.

![](examples/bootstrap/menu.html)


## Bootstrap tables
{id: bootstrap-tables}
{i: table}
{i: table-striped}
{i: table-hover}

[tables](http://getbootstrap.com/css/#tables)


![](examples/bootstrap/tables.html)


## Bootstrap form elements
{id: bootstrap-forms}


[forms](http://getbootstrap.com/css/#forms)

![](examples/bootstrap/forms.html)


## Lead Paragraph
{id: bootstrap-lead-paragraph}

![](examples/bootstrap/lead_paragraph.html)


## Bootstrap Grid is Responsive
{id: bootstrap-responsive-grid}

![](examples/bootstrap/responsive_grid.html)


## Bootstrap Grid can be hidden
{id: bootstrap-responsive-grid-hide}

![](examples/bootstrap/responsive_grid_hide.html)


## Bootstrap Grid hide the side when small
{id: bootstrap-responsive-grid-hide-side}

![](examples/bootstrap/responsive_grid_hide_margin.html)


## Exercises: Bootstrap
{id: exercises-bootstrap}


Take the previous examples (e.g. the TODO app) and change it to use Bootstrap.

* Convert the form elements
* Replace the error style with an 'alert alert-warning' class
* Add a Glyphicon to the save button and replace the 'x' for delete by another Glyphicon


# CSS - Cascading Style Sheets
{id: mobile-css}

## Introduction to CSS
{id: introduction-to-css}
{i: CSS}

* Where to put CSS
* Basic selectors: tag, id, class
* Properties, values



## CSS in elements
{id: css-in-elements}

* CSS can be added to individual HTML elements.
* CSS can be embedded in the HTML file in a separate section.
* CSS can be included from an external file.

![](examples/css/intro_in_tag.html)


## Embedded CSS
{id: embedded-css}
![](examples/css/intro_embedded.html)


## External CSS
{id: external-css}
![](examples/css/intro.html)
![](examples/css/intro.css)


## Basic Selectors
{id: basic-css-selectors}

* HTML tag
* HTML attributes: id, class

![](examples/css/basic-selectors.html)
![](examples/css/basic-selectors.css)


## Descendant and Child CSS Selectors
{id: css-selectors}
![](examples/css/selectors.html)
![](examples/css/selectors.css)


List of selectors: <a href="http://www.w3.org/TR/CSS2/selector.html"></a>




## div and span
{id: div-and-span}

* div  (block level)
* span (inline)
* <a href="http://en.wikipedia.org/wiki/Span_and_div"></a>

![](examples/css/div-and-span.html)


## Layouts
{id: layouts}

* Static layout
* Dynamic layout



* Fixed-width
* Relative
* Fluid
* Elastic
* Hybrid
* Responsive


{aside}
What happens when the width is fixed? Horizontal scrollbar or picture disappearing.
{/aside}



## Fixed width and text
{id: css-fixed-width-and-text}
![](examples/css/fixed-width-text.css)
![](examples/css/fixed-width-text.html)


## Relative width and text
{id: css-relative-width-and-text}
![](examples/css/relative-width-text.css)
![](examples/css/relative-width-text.html)


## Fixed Image
{id: css-fixed-image}

The actual image is 1280 x 716

![](examples/css/fixed-image.css)
![](examples/css/fixed-image.html)



## Media Query
{id: css-media-query}
{i: media query}
{i: @media}

Change CSS based on


* min-width
* max-width
* min-height
* max-height
* min-device-height
* max-device-height
* device-aspect-ratio
* orientation (portrait or landscape)
* ...



You can use <emp>and</emp>, and the comma <emp>,</emp> to indicate <emp>or</emp> and even the word <emp>not</emp> to have the full
power of boolean expressions.




You can use @media queries inside a single style-sheet, or you can load different style-sheets base on the @media query.





Probably the most common thing to use @media queries for is to change the site depending on the width of the browser
using the min-width and max-width fields, but you can also use the others listed above.




Of course you can also use it to check the media type: screen, print, etc.
<a href="http://css-tricks.com/css-media-queries/"></a>




## Resize image
{id: css-media-query-resize-image}
![](examples/css/media-query-images-resizing.html)
![](examples/css/images-resizing.css)


## Replace image
{id: css-media-query-replace-image}
![](examples/css/replace-image.html)
![](examples/css/replace-image.css)


<a href="http://css-tricks.com/css-image-replacement/"></a>





## Colors
{id: css-media-query-colors}
![](examples/css/colors.css)
![](examples/css/media-query-colors.html)



## CSS3
{id: css3}

More standardization


* Rounded Corners (easier)
* Background Decoration
* New Colors schemes
* Text Effects: e.g. text-shadow
* More powerful selectors (attribute mathching)
* Transitions
* Media Queries



## Rounded corners
{id: rounded-corners}
![](examples/css/rounded-corners.html)


<a href="http://css-tricks.com/snippets/css/rounded-corners/"></a>








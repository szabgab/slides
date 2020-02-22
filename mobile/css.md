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

![](examples/csses/intro_in_tag.html)


## Embedded CSS
{id: embedded-css}

![](examples/csses/intro_embedded.html)


## External CSS
{id: external-css}

![](examples/csses/intro.html)
![](examples/csses/intro.css)


## Basic Selectors
{id: basic-css-selectors}

* HTML tag
* HTML attributes: id, class

![](examples/csses/basic-selectors.html)
![](examples/csses/basic-selectors.css)


## Descendant and Child CSS Selectors
{id: css-selectors}

![](examples/csses/selectors.html)
![](examples/csses/selectors.css)


[List of selectors](http://www.w3.org/TR/CSS2/selector.html)


## div and span
{id: div-and-span}

* div  (block level)
* span (inline)
* [span and div](http://en.wikipedia.org/wiki/Span_and_div)

![](examples/csses/div-and-span.html)


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

![](examples/csses/fixed-width-text.css)
![](examples/csses/fixed-width-text.html)


## Relative width and text
{id: css-relative-width-and-text}

![](examples/csses/relative-width-text.css)
![](examples/csses/relative-width-text.html)


## Fixed Image
{id: css-fixed-image}

The actual image is 1280 x 716

![](examples/csses/fixed-image.css)
![](examples/csses/fixed-image.html)



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

You can use `and`, and the comma `,` to indicate `or` and even the word `not` to have the full
power of boolean expressions.

You can use **@media queries** inside a single style-sheet, or you can load different style-sheets base on the @media query.

Probably the most common thing to use @media queries for is to change the site depending on the width of the browser
using the min-width and max-width fields, but you can also use the others listed above.


Of course you can also use it to check the media type: screen, print, etc.
[css media queries](http://css-tricks.com/css-media-queries/)


## Resize image
{id: css-media-query-resize-image}

![](examples/csses/media-query-images-resizing.html)
![](examples/csses/images-resizing.css)


## Replace image
{id: css-media-query-replace-image}

![](examples/csses/replace-image.html)
![](examples/csses/replace-image.css)


[css image replacement](http://css-tricks.com/css-image-replacement/)


## Colors
{id: css-media-query-colors}
![](examples/csses/colors.css)
![](examples/csses/media-query-colors.html)



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

![](examples/csses/rounded-corners.html)

[rounded corners](http://css-tricks.com/snippets/css/rounded-corners/)


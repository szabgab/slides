# CSS intro
{id: css-intro}


## What is CSS for?
{id: what-is-css-for}

* Provide a relatively easy way to change how a group of HTML pages look like.


{aside}

Each CSS rule is a combination of a **selector** that selects to which specific element the rule applies to.
(for example the a element within a p element that is in the "news" class.)

An attribute  (for example color).

And a values for that attribute. (For example red.)

p.news a {
  color: red;
}
{/aside}


## How to add CSS to an HTML document?
{id: how-to-add-css-to-an-html-document}

* Inline style attribute
* In the &lt;head&gt; tag or in the &lt;body&gt; of the HTML
* In a separate file using &lt;link&gt;



## Inline style attribute
{id: inline-style-attribute}
![](examples/css/inline.html)

{aside}
In order to see this, save the code in a file with .html extension and open it with a browser.
{/aside}



## In the head or body of the  HTML
{id: in-head-or-body}
![](examples/css/in_head_or_body.html)


## External stylesheet included with a link
{id: external-stylesheet}
![](examples/css/external.html)
![](examples/css/external.css)

{aside}
In most cases people place the link tag inside the head tag, but it also works outside of it.
{/aside}




## background
{id: background}

```
selector {
   background-color: #FFFFFF;
   background-image: url("path/to/image.png") | none;
   background-repeat: repeat | no-repeat | repeat-x | repeat-y;

   background: #FFFFFF none;
}
```



## Learn layout
{id: learnlayout}

* [Learn layout here!](http://learnlayout.com/) inspired the following pages.


## No layout
{id: no-layout}

![](examples/css/no_layout.html)


## margin: auto
{id: margin-auto}
{i: margin: auto}
{i: width}
{i: max-width}

![](examples/css/margin_auto.html)


## box-sizing
{id: box-sizing}
{i: box-sizing}

![](examples/css/box_sizing.html)



## display
{id: display}
{i: display}
{i: block}
{i: inline}
{i: none}

{aside}

The default display property of div, p , form, header, footer, section, and li is 'block'.
The default display property of span and a is 'inline'.
{/aside}

```
```


## position
{id: position}
{i: position}
{i: static}
{i: relative}
{i: fixed}
{i: absolute}

* static - the default = has no position
* relative - it is relative to where it should be if it was static. The relativity is set by top/left/right/bottom
* 
* 
* 



## boxes using div
{id: boxes-using-div}

![](examples/css/boxes.html)



## Resources
{id: resources}

* [Learn layout](http://learnlayout.com/)
* [CSS Font stack](http://cssfontstack.com/)



## modal
{id: modal}

![](examples/css/modal.html)


source: http://netdna.webdesignerdepot.com/uploads7/creating-a-modal-window-with-html5-and-css3/demo.html







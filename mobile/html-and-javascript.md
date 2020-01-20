# HTML and Javascript
{id: html-and-javascript}

## Document Object Model(DOM)
{id: dom}
{i: DOM}

The DOM is a hierarchy of objects.



## getElementById and innerHTML
{id: get-element-by-id}
{i: getElementById}
{i: innerHTML}
![](examples/javascript/get_element_by_id.html)


## getElementsByTagName
{id: get-element-by-tagname}
{i: getElementsByTagName}
![](examples/javascript/get_elements_by_tag_name.html)


## getElementsByClassName
{id: get-element-by-classname}
{i: getElementsByClassName}
![](examples/javascript/get_elements_by_class_name.html)


## Events handling
{id: events-handling}

* Mouse: click
* Keyboard: keypress
* Interface Events: load, scroll. resize
* Form: select, change, submit, reset, focus, blur
* Touch: touchstart, touchend, touchmove, touchenter, touchleave, touchcancel
* <a href="http://en.wikipedia.org/wiki/DOM_Events"></a>





## Add event listener
{id: add-event-handler}
{i: addEventListener}
{i: removeEventListener}
{i: dispatchEvent}

```
  element.onevent =
  element.attachEvent()       (IE)
  element.addEventListener()   (everything else including IE9 and above)
```


## Example for using event objects
{id: event-object-old}

old style

![](examples/javascript/event_old.html)


## Example for using event objects
{id: event-object-new}

new style

![](examples/javascript/event_new.html)


## Schedule event
{id: schedule-an-event}
{i: setTimeout}
![](examples/javascript/schedule_event.html)


## Exercise: Update button
{id: exercise-events-upodate-button}


Modify the previous example so when the user clicks on the button,
the text on it will be updated to 'Clicked'.




Once that's done, change the solution again, so 2 seconds later the text on the button will change back to the original text.




## Exercise events
{id: exercise-events}


Create a page with two text input boxes and a button.
Allow the user to type in one of the boxes.

When text changes in one of the boxes, change the text in the other box as well.




## Solution for update button
{id: solution-events-button}
![](examples/javascript/event_new_update.html)


## Solution for update and reset button
{id: solution-events-button-reset}
![](examples/javascript/event_new_update_reset.html)



## Solution
{id: solution-events}
![](examples/javascript/event_update_on_click.html)


## DOM API Allows
{id: dom-api-allows}

* Getting info on elements
* Chaning element attributes
* Creating new elements
* Setting elements style







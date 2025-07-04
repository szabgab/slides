# Selenium locator

* Selenium::Remote::WebElement}
* find_element}
* default_find}


[Selenium::Remote::WebElement](https://metacpan.org/pod/Selenium::Remote::WebElement)


```
find_element(SEARCH_STRING, [MODE])
return a Selenium::Remote::WebElement object of the first matched element.

MODE:
   class
   class_name
   css
   id
   link
   link_text
   partial_link_text
   tag_name
   name
   xpath

MODE defaults to xpath
default mode can be set via the 'default_finder' parameter of the constructor.
```





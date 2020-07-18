# DOM - Document Object Model
{id: dom}

## Inject content in HTML
{id: display-embedded-html}
{i: getElementById}
{i: innerHTML}
![](examples/dom/inject_content.html)
![](examples/dom/inject_content.js)



## Add event listener
{id: add-event-listener}
{i: addEventListener}
![](examples/dom/add_event_listener.html)
![](examples/dom/add_event_listener.js)


## Get value of input box
{id: get-value-of-input-box}
![](examples/dom/get_value_of_input_box.html)
![](examples/dom/get_value_of_input_box.js)


## Get value of selected option
{id: get-value-of-selected-option}
{i: selectedIndex}
{i: getElementById}
{i: addEventListener}
{i: click}
![](examples/dom/get_selected_option.html)
![](examples/dom/get_selected_option.js)


## Update selection box based on other selection
{id: javascript-update-selection-box}
![](examples/js/update_form.html)
![](examples/js/update_form.js)

```
```


## Autoresizing Grid
{id: grid}
![](examples/js/grid.html)


## Local storage - counter
{id: local-storage-counter}
![](examples/js/local_storage_counter.html)


## Remove item from local storage - reset counter
{id: local-storage-reset-counter}
![](examples/js/local_storage_counter_reset.html)


## Clear local storage
{id: clear-local-storage}

Remove all the data from the local storage


```
localStorage.clear();
```


## Local storage - boolean
{id: local-storage-boolean}
{i: JSON}

{aside}
In many browsers local storage can only store string. So when we store the boolean true or false, it actually stores
the strings "true" or "false". In order to get back the real boolean values, we can use the JSON.parse() method.
{/aside}
![](examples/js/local_storage_boolean.html)





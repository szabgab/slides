# JavaScript Objects
{id: javascript-objects}

## new empty object
{id: new-empty-object}
![](examples/objects/new_empty_object.js)


## new Objects
{id: new-object}
![](examples/objects/new_object.js)


## new Object with attribute
{id: new-object-attribute}
![](examples/objects/new_object_with_attribute.js)


## Literal Objects
{id: object}
{i: object}
{i: hash}
{i: dictionary}

{aside}
Keys in the object don't need to be quoted, unless they contain special characters, like a dash.
{/aside}

![](examples/objects/object.js)

```
Object { from: "js@bar.com", to: Array[2], subject: "Hello World", mime-type: "text" }
```


## Dumping data structures (for debugging)
{id: dumping-data-structures}
{i: JSON}
{i: Dump}
![](examples/objects/dumping_data_structures.js)

```
"{
  "name": "Foo Bar",
  "emails": [
    "foo@bar.com",
    "foobar@gmail.com"
  ]
}"
```


## Access JavaScript object attributes
{id: access-javascript-object-attributes}
![](examples/objects/object_attributes.js)

```
"{
  "from": "js@bar.com",
  "to": [
    "foo@bar.com",
    "qux@bar.com"
  ],
  "subject": "Hello World",
  "mime-type": "text",
  "text": "Content"
}"
```


## Change JavaScript object attributes
{id: change-javascript-object-attributes}
![](examples/objects/change_object.js)


## Add JavaScript object attributes
{id: add-javascript-object-attributes}
![](examples/objects/add_object_attribute.js)


## Delete property from object
{id: delete-property-from-object}
{i: delete}
![](examples/objects/delete.js)


## for-in loop on JavaScript object
{id: for-in-loop-on-javascript-object}
{i: for in}
{i: hasOwnProperty}
![](examples/objects/for_in_loop_on_object.js)


## Count words
{id: count-words}
![](examples/objects/count_words.js)

'constructor' needs special treatment as that attribute is already part of the object.



## Count words fixed
{id: count-words-fixed}
![](examples/objects/count_words_fixed.js)


## keys of an object
{id: keys}
{i: keys}
![](examples/objects/keys.js)




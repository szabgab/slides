# Classes
{id: classes}

## Empty Class definition
{id: empty-class-definition}
{i: class}

![](examples/classes/empty_class.cr)


## Class with attributes
{id: class-with-attributes}
{i: initialize}
{i: @}

![](examples/classes/person_class.cr)


## Class with getters
{id: class-with-getters}

![](examples/classes/class_with_getters.cr)

## Class with setter
{id: class-with-setters}

![](examples/classes/class_with_setters.cr)


## Class with getters and setter (property)
{id: class-with-getters-and-setters}
{i: property}
{i: getter}

![](examples/classes/class_with_property.cr)


## Class with property with default value
{id: class-with-property-with-default-value}
{i: property}

![](examples/classes/class_with_default_property.cr)


## Class with declated getter and default value
{id: class-with-declared-getter-and-default-value}
{i: getter}

![](examples/classes/class_with_declared_getter_default.cr)


## Class with declated getter
{id: class-with-declared-getter}
{i: getter}

![](examples/classes/class_with_declared_getter.cr)


## Serialize Crystal-lang class to/from JSON from_json to_json
{id: class-serialization-to-from-json}
{i: to_json}
{i: from_json}
{i: JSON::Serializable}


* [JSON::Serializable](https://crystal-lang.org/api/JSON/Serializable.html)

![](examples/classes/class_and_json.cr)


## Compare objects for equality
{id: compare-objects-for-equality}

Normally using `==` between two instances will only return `true` if they are the exact same objects in the memory.
If "only" all the attributes are the same then `==` will be `false`.

To be able to compare two objects based on their attributes only we can used the `def_equals` macro.

* [Object](https://crystal-lang.org/api/Object.html)

![](examples/classes/compare_objects.cr)

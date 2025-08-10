# Add timestamp to item (back-end TO_JSON)

```
Route exception: encountered object '2015-06-08T16:08:05',
but neither allow_blessed, convert_blessed nor allow_tags settings are enabled
(or TO_JSON/FREEZE method missing
```

Run the tests

{% embed include file="src/examples/snippets/10/test_output.txt" %}
{% embed include file="src/examples/snippets/10/prove.txt" %}

Tell MongoDB to use DateTime::Tiny


```
$client->dt_type( 'DateTime::Tiny' );
```
{% embed include file="src/examples/snippets/10/prove2.txt" %}



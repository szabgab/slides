# Units: em (The size of Letter M)

Relative to the font-size of the element.

{% embed include file="src/examples/html/page_em.html" %}
{% embed include file="src/examples/html/page_em.css" %}


The problem will be if we add another css directive insied the 'p' directive. eg. 'border 1em solid red'.
In this case the 1em will be relative to the font size of the 'p' element and not the font-size of the 'html'
element. So within the same 'p' element '2emp' of the 'font-size' and '1em' of the 'border' will be equal.


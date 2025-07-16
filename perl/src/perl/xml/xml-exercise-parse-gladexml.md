# Exercise: parse glade.xml

{% embed include file="src/examples/xml/entry.glade)

Given the XML file created by Glade write the following functions:

```perl
my @names   = get_all_widget_names(); # all the names
my @widgets = get_all_widges();       # all the objects
my $widget  = get_widget($name);      # an object representing the widget
$widget->get_handler($name);          # name of the handler function
$widget->get_property($name);
$widget->set_property($name, $value);
```



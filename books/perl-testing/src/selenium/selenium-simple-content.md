# Selenium content

* server_is_running}
* body_text_contains}
* content_contains}
* get_text}
{% embed include file="src/examples/www/selenium_content.t" %}

* body_text_contains - disregard HTML element
* content_contains - check in the raw HTML
* find_element will throw exception if cannot find element
* find_element_ok of the test module can only use the default locator



content_* methods


* $s->content_like($regex [,$desc])
* $s->content_unlike($regex [,$desc])
* $s->content_contains( $str [, $desc ] )
* $s->content_lacks( $str [, $desc ] )



body_text_*


* $s->body_text_like( $regex [, $desc ] )
* $s->body_text_unlike( $regex [, $desc ] )
* $s->body_text_contains( $str [, $desc ] )
* $s->body_text_lacks( $str [, $desc ] )






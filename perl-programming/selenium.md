# Selenium
{id: selenium}

## Selenium documentation
{id: selenium-docs}
{i: Selenium}

* [Selenium](http://docs.seleniumhq.org/)
* [Selenium::Remote::Driver](https://metacpan.org/pod/Selenium::Remote::Driver)
* [Test::Selenium::Remote::Driver](https://metacpan.org/pod/Test::Selenium::Remote::Driver)
* [Selenium::Remote::Driver wiki](https://github.com/gempesaw/Selenium-Remote-Driver/wiki)
* [Selenium tutorial](http://birmingham.pm.org/talks/barbie/selenium/) by Barbie
* [Selenium tutorial](http://www.perlmonks.org/?node_id=720018) on PerlMonks 
* Using Firefox install [Selenium IDE ](http://docs.seleniumhq.org/download)



## Selenium IDE
{id: selenium-ide}
{i: Selenium IDE}

* [Download xpi file](http://docs.seleniumhq.org/download/) of version 2.5.0 using FireFox
* [Login/Logout](http://blogs.perl.org/)
* [Login/Change Profile/Logout](http://blogs.perl.org/)
* [Login/Change Profile/Verify Result/Logout](http://blogs.perl.org/)
* The company web site
* [YAPC::EU](http://act.yapc.eu/ye2014/) (select one of the talks)


{aside}

Reset web site to the point we need to start testing.
{/aside}

{aside}

We can install the Selenium IDE in Firefox, record a session
interacting with a web site and then we can replay it with Firefox.

We start the recording by click on Tools/Selenium IDE.
A new window will show, that is the Selenium IDE. We'll
be able to stop the recording by pressing the red button.
Then we can export the recorded script in several languages.
{/aside}


## Launch Selenium server
{id: launch-selenium-server}


Download the jar file from [Selenium HQ](http://docs.seleniumhq.org/download/).

```
java -jar /home/gabor/Downloads/selenium-server-standalone-2.42.2.jar
```

## Selenium DuckDuckGo
{id: selenium-duckduckgo}
{i: Selenium::Remote::Driver}
{i: get}
{i: get_title}
{i: quit}

[Selenium::Remote::Driver](https://metacpan.org/pod/Selenium::Remote::Driver)

![](examples/www/selenium_ddg.pl)


## Selenium using Chrome
{id: selenium-using-chrome}
{i: Chrome}
{i: browser_name}


Follow the instructions in the [wiki](https://github.com/gempesaw/Selenium-Remote-Driver/wiki/Chrome-browser-automation)




<command>java -Dwebdriver.chrome.driver="/home/gabor/Downloads/chromedriver" -jar /home/gabor/Downloads/selenium-server-standalone-2.42.2.jar</command>


![](examples/www/selenium_ddg_chrome.pl)



## Selenium DuckDuckGo Search
{id: selenium-duckduckgo-search}
{i: find_element}
{i: Selenium::Remote::WDKeys}
{i: KEYS}
{i: send_keys}

[Selenium::Remote::WDKeys](https://metacpan.org/pod/Selenium::Remote::WDKeys)

![](examples/www/selenium_ddg_search.pl)


## Selenium DuckDuckGo Test
{id: selenium-duckduckgo-test}
{i: Test::Selenium::Remote::Driver}
{i: get_ok}
{i: title_is}
{i: body_text_contains}

[Test::Selenium::Remote::Driver](https://metacpan.org/pod/Test::Selenium::Remote::Driver)

![](examples/www/selenium_ddg_search.t)


## Selenium locator
{id: selenium-locator}
{i: Selenium::Remote::WebElement}
{i: find_element}
{i: default_find}


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


## Selenium locator example
{id: selenium-locator-example}

Run **perl examples/www/server/server.pl** for the sample web application.

![](examples/www/selenium_locate.t)


## Selenium content
{id: selenium-simple-content}
{i: server_is_running}
{i: body_text_contains}
{i: content_contains}
{i: get_text}
![](examples/www/selenium_content.t)

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




## Selenium in the calc example
{id: selenium-simple-example}
![](examples/www/selenium_calc.t)


## Selenium examples with JavaScript
{id: selenium-examples-with-javascript}
![](examples/www/selenium_server.t)


## Selenium examples with Ajax
{id: selenium-examples-with-ajax}
![](examples/www/selenium_ajax.t)


## WWW::Mechanize::PhantomJS
{id: www-mechanize-phantomjs}
{i: WWW::Mechanize::PhantomJS}


Speed up Selenium with [PhantomJS](http://phantomjs.org/) which is a headless Webkit browser
using [GhostDriver](https://github.com/detro/ghostdriver) and
[WWW::Mechanize::PhantomJS](https://metacpan.org/pod/WWW::Mechanize::PhantomJS).


![](examples/phantom/google.pl)
![](examples/phantom/localhost.pl)


## Testing Dancer
{id: dancer}
![](examples/webapp/test.t)
![](examples/webapp/Test.pm)


## Exercies: MetaCPAN
{id: exercise-metacpan}

* Visit [MetaCPAN](http://metacpan.com/), search for something and observe the links. Has the small logo appeared?
* Visit [Expect](https://metacpan.org/pod/Expect), click on 'Jump to version' and select 1.25. It should go here: [Expect](https://metacpan.org/pod/release/SZABGAB/Expect-1.25/lib/Expect.pm)
* Visit MetaCPAN, can you automate logging in?


## Exercise: blogs.perl.org
{id: exercise-blogs-perl-org}


Test [blogs](http://blogs.perl.org/). You can also contribute test cases to [my tests](https://github.com/szabgab/test.blogs.perl.org).


## Exercise: Testing Smolder
{id: exercise-test-smolder}


In an earlier chapter we used Smolder to collect results of the test executions.
Smolder itself is a web application using Javascript. Let's test it.

Let's start by assuming smolder is running and try to access its front page and login with
an existing user.

Then we should try to create a new user and log in with that.

After that, as we cannot really know which user is still available let's
create a new .smolder directory in some temporary place (use File::Temp for this).
Create a configuration file, launch Smolder and then access it using your test script.


## Exercise: Act
{id: exercise-with-act}

Take the script logging in to Act and change it to use Tess::WWW::Mechanize


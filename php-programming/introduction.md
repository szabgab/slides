# PHP
{id: php}

## About - History
{id: php-about}

* Originally written and released by Rasmus Lerdorf in 1995
* PHP/FI
* Personal Home Page Tools or Personal Home Page / Forms Interpreter
* PHP 3.0 written and relased by Andi Gutmans and Zeev Suraski (ZEND) in 1997
* PHP 4.0 Released in 1999-2000
* PHP 5.0 Released in 2004
* PHP 5.5.10 Released on 6 Marh 2014
* PHP 5.6 is on its way
* [History](http://www.php.net/manual/en/history.php)
* [PHP news](http://www.php.net/)



## HTTP: A few words about how the web works
{id: http}

* Browser -> HTTP Request -> Web Server (Apache, IIS, Nginx)
* Web Server -> HTTP Response -> Browser
* Simple response: Content of file as is (HTML, image, etc.)
* CGI Response: Execute the file and return its output
* PHP: Pass the file to the PHP Engine that runs within Apache
* Others: JSP, ASP, mod_perl



## Hello world
{id: php-hello-world}
{i: echo}
{i: &lt;?php}
{i: .php}

{aside}

Embedded in an html file, code between &lt;?php and ?&gt; tags is executed as PHP code. The result printed by that code is embedded in the HTML page.
While the mapping of URLs to files is configurable in the web server, PHP files usually end with the **php** extension.
{/aside}
![](examples/intro/hello_world.php)


## Hello world, no HTML
{id: php-hello-world-no-html}

{aside}
There is not even need for html around the code...
{/aside}

![](examples/intro/hello_world_no_html.php)


## HTML inside PHP
{id: html-inside-php}
![](examples/intro/html_in_php.php)


## phpinfo
{id: php-phpinfo}
{i: phpinfo}
![](examples/intro/phpinfo.php)


## Comments
{id: php-comments}
{i: #}
{i: /*}
![](examples/intro/comments.php)


## Errors
{id: php-errors}

Check how syntax error will look like

![](examples/intro/errors.php)

```
Parse error: parse error in .../examples/intro/errors.php on line 4
```


## print vs echo
{id: print-vs-echo}
{i: print}
{i: echo}

{aside}

**echo** can get several parameters, **print** can only get one.
{/aside}
![](examples/intro/print_vs_echo.php)



## Numbers
{id: numbers}
{i: 0}
{i: 0x}
![](examples/intro/numbers.php)


## Numerical Operations
{id: php-simple-calculations}
{i: +}
{i: -}
{i: *}
{i: /}
![](examples/intro/simple_computation.php)


## Strings - concatenation
{id: strings}
{i: "}
{i: .}
![](examples/intro/strings.php)


## Variables
{id: scalar-variables}

{aside}
Hold either numbers or strings. There is no need to declare the variable, nor is there a type involved.
{/aside}

![](examples/intro/variables.php)


## Variable interpolation (or variable expansion)
{id: variable-interpolation}
{i: '}

{aside}

It happens in strings in double-quotes, but not in strings in single-quotes.
{/aside}
![](examples/intro/variable_interpolation.php)


## String functions
{id: string-functions}
{i: strcmp}
{i: strcasecmp}
{i: explode}
{i: implode}
{i: nl2br}
{i: file_get_contents}
{i: str_replace}
{i: iconv}
{i: urlencode}


There are lots of string functions in PHP. Here are a few examples:



* strcmp - compare two string returns, -1, 0 +1 based on order according to ASCII table
* strcasecmp
* explode - split string to elements and return an array
* implode - join array to make a string
* nl2br - new line to html-break
* file_get_contents - read in a whole file without explicitely opening (slurp)
* str_replace - replace characters in a string
* iconv - convert between character encodings: iconv('ISO-8859-8', 'UTF-8', $str)
* urlencode - when we are generating URLs some characters (e.g. space) need to be encoded



## addslashes
{id: addslashes}
{i: addslashes}

{aside}
Escaping special characters such as '
{/aside}

![](examples/intro/addslashes.php)

{aside}

[addslashes](http://php.net/manual/en/function.addslashes.php)
{/aside}


## stripslashes
{id: stripslashes}
{i: stripslashes}
![](examples/intro/stripslashes.php)


## trim - remove white spaces from both ends of a string
{id: trim}
{i: trim}
{i: ltrim}
{i: rtrim}
![](examples/intro/trim.php)

{aside}

[trim](http://php.net/manual/en/function.trim.php)
White space characters are \n, \r, \t and space itself.
ltrim is left trim, rtrim is right trim.
{/aside}





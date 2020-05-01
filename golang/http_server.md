# HTTP Server
{id: http-server}


## HTTP Hello World
{id: http-hello-world}
{i: http}
{i: ListenAndServe}
{i: ResponseWriter}
{i: Request}

* [net/http](https://golang.org/pkg/net/http/)

![](examples/http-hello-world/http_hello_world.go)

## HTTP Echo GET
{id: http-echo-get}
{i: GET}
{i: FormValue}

![](examples/http-echo-get/http_echo_get.go)

## HTTP Echo POST
{id: http-echo-post}
{i: POST}
{i: PostFormValue}
{i: Method}

![](examples/http-echo-post/http_echo_post.go)

## text/template
{id: text-template}

* [text/template](https://golang.org/pkg/text/template/)

{aside}
The `New` call gets a string that becomes the name of this template. I am not sure where is that name used again.
{/aside}

![](examples/text-template/text_template.go)


## text/template with map
{id: text-template-map}

![](examples/text-template-map/text_template_map.go)

## text/template with struct
{id: text-template-struct}


![](examples/text-template-struct/text_template_struct.go)

## text/template in file
{id: text-template-in-file}

![](examples/text-template-file/text_template_file.go)
![](examples/text-template-file/main.txt)

![](examples/text-template-file/text_template_file.out)

## text/template if
{id: text-template-if}

![](examples/text-template-if/text_template_if.go)
![](examples/text-template-if/if.txt)

![](examples/text-template-if/text_template_if.out)

## text/template loop
{id: text-template-loop}

![](examples/text-template-loop/text_template_loop.go)
![](examples/text-template-loop/loop.txt)

![](examples/text-template-loop/text_template_loop.out)


## html/template
{id: html-template}

* [html/template](https://golang.org/pkg/html/template/)
* Based on text/template so it has the same API.
* Automatically escapes dangerous characters.

![](examples/html-template/html_template.go)


## HTTP Hello World templates
{id: http-hello-world-templates}

![](examples/http-hello-world-template/http_hello_world_template.go)
![](examples/http-hello-world-template/main.html)


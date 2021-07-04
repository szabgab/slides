# Kemal
{id: kemal}

## About Kemal
{id: kemal-about}

* [Kemal](https://kemalcr.com/)
* Created by Serdar Dogruyol

## Kemal Install
{id: kemal-install}

Create a directory and create the following file in it:

![](examples/kemal/shard.yml)

Run the following command in the directory

```
shards install
```

If it fails with
`Failed to resolve dependencies, try updating incompatible shards or use --ignore-crystal-version as a workaround if no update is available.`

then try this:

```
shards install --ignore-crystal-version
```

## Hello World
{id: kemal-hello-world}

![](examples/kemal/src/hello_world.cr)

```
crystal src/hello_world.cr
```

```
http://localhost:3000/
```

## Testing Hello World
{id: kemal-testing-hello-world}


![](examples/kemal/spec/hello_world_spec.cr)

```
crystal spec/hello_world_spec.cr
```

## Kemal Autorestart (autoreload)
{id: kemal-autorestart}

```
crystal build --release lib/sentry/src/sentry_cli.cr -o ./bin/sentry
./bin/sentry -b "crystal build src/webapp.cr -o bin/webapp" -r bin/webapp
```
![](examples/kemal/src/webapp.cr)

## Kemal GET parameters
{id: kemal-get-parameters}
{i: GET}

![](examples/kemal/src/get_params.cr)

![](examples/kemal/spec/get_params_spec.cr)

```
crystal spec/get_params_spec.cr
```

## Kemal POST parameters
{id: kemal-post-parameters}
{i: POST}

![](examples/kemal/src/post_params.cr)

![](examples/kemal/spec/post_params_spec.cr)

```
crystal spec/post_params_spec.cr
```

## Kemal Route parameters
{id: kemal-route-parameters}

![](examples/kemal/src/route_params.cr)

![](examples/kemal/spec/route_params_spec.cr)

```
crystal spec/post_params_spec.cr
```

## Kemal ECR Templates
{id: kemal-ecr-templates}

* [ECR](https://crystal-lang.org/api/ECR.html)

![](examples/kemal/src/ecr_template.cr)
![](examples/kemal/src/views/page.ecr)
![](examples/kemal/src/views/layouts/layout.ecr)

## Kemal with Jinja templates
{id: kemal-jinja-templates}

* [Jinja](https://jinja.palletsprojects.com/) (Python)
* [Crinja](https://straight-shoota.github.io/crinja/)

![](examples/kemal/src/jinja.cr)
![](examples/kemal/src/views/home.html.j2)


## Kemal Elapsed time
{id: kemal-elapsed-time}

![](examples/kemal/src/elapsed_time.cr)
![](examples/kemal/src/views/layouts/layout_with_elapsed_time.ecr)
![](examples/kemal/src/views/time.ecr)

## Accept GET, POST, and route parameter in the same POST route
{id: kemal-get-post-route}

![](examples/kemal/src/params.cr)
![](examples/kemal/spec/params_spec.cr)


## Kemal indicate 404
{id: kemal-indicate-404}

![](examples/kemal/src/send_404.cr)

![](examples/kemal/spec/send_404_spec.cr)

## Kemal Styling 404 pages
{id: kemal-styling-404-pages}

![](examples/kemal/src/customized_404.cr)
![](examples/kemal/spec/customized_404_spec.cr)

## Kemal set headers (change content-type)
{id: kemal-set-header}

![](examples/kemal/src/set_header.cr)
![](examples/kemal/spec/set_header_spec.cr)

## Kemal redirect
{id: kemal-redirect}

## Kemal in Docker
{id: kemal-in-docker}


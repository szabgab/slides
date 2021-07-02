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

## Kemal Autorestart
{id: kemal-autorestart}

## Kemal GET parameters
{id: kemal-get-parameters}

![](examples/kemal/src/get_params.cr)

![](examples/kemal/spec/get_params_spec.cr)

```
crystal spec/get_params_spec.cr 
```

## Kemal POST parameters
{id: kemal-post-parameters}

## Kemal Route parameters
{id: kemal-route-parameters}

## Kemal Any Route parameters
{id: kemal-any-route-parameters}

## Kemal Templates
{id: kemal-templates}

* Templates
* Jinja templates
* GET
* POST
* Elapsed time

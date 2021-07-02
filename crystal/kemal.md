# Kemal
{id: kemal}

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

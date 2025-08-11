# Kemal Install

Create a directory and create the following file in it:

{% embed include file="src/examples/kemal/shard.yml)

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



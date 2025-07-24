# Metadata on the instance

* Compute Engine - VM instances - (instance) - edit
* Custom metadata
* Set 'hello' : 'world'

```
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/hello
```



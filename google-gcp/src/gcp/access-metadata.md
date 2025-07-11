# Access Metadata

* On the instance:

```
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/hostname
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/name
```



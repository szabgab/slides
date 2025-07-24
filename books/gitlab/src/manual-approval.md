# Manual approval


* Click on the `gear` as variable type in `CODE` and as value type in `secret`.

```yaml
{{#include ../examples/pipelines/manual-approval/.gitlab-ci.yml}}
```


To generate such a secret hash use the following command on linux:

```
echo "'$(echo -n secret | sha256sum)'"
```



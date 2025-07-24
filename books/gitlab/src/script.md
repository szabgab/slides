# Script


* **script:** it is required and it can be a single command or an array of commands
* **before_script** and **after_script** are both optional, but if they exists they must be arrays (even if there is only one element)
* You can have `before_script` and `after_script` as a main-key in the YAML file.
* A job that does not have `before_script` will inherit the central `before_script`. Same with `after_script`.

```yaml
{{#include ../examples/pipelines/steps/.gitlab-ci.yml}}
```


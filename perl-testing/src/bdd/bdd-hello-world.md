# BDD Hello World


```
examples/bdd/
└── basic
    ├── features
    │   ├── basic.feature
    │   └── step_definitions
    │       └── some_steps.pl
    └── lib
        └── HelloWorld.pm
```

{% embed include file="src/examples/bdd/basic/features/basic.feature)
{% embed include file="src/examples/bdd/basic/features/step_definitions/some_steps.pl" %}
{% embed include file="src/examples/bdd/basic/lib/HelloWorld.pm" %}

```
pherkin examples/bdd/basic/
prove -v  -r --source Feature --ext=.feature examples/bdd/basic/
```



# BDD - Behavior Driven Development
{id: bdd}


## BDD Hello World
{id: bdd-hello-world}

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

![](examples/bdd/basic/features/basic.feature)
![](examples/bdd/basic/features/step_definitions/some_steps.pl)
![](examples/bdd/basic/lib/HelloWorld.pm)

```
pherkin examples/bdd/basic/
prove -v  -r --source Feature --ext=.feature examples/bdd/basic/
```

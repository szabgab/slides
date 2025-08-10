# Add header: Access-Control-Allow-Methods

Add to the before hook of lib/D2/Ajax.pm:


```
header 'Access-Control-Allow-Methods' => 'GET, POST, OPTIONS, DELETE';
```

Add to lib/D2/Ajax.pm


```
options '/api/v2/item/:id' => sub {
    return '';
};
```

Test it:

{% embed include file="src/examples/snippets/8/t/options.t" %}



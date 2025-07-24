# Deploy using Git commit webhooks

* Go to GitHub repository
* Settings
* Webhooks

```
Payload URL: https://deploy.hostlocal.com/
Content tpe: application/json
Secret: Your secret
```

{% embed include file="src/examples/deploy/webhook.py" %}



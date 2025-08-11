# Kemal Autorestart (autoreload)

```
crystal build --release lib/sentry/src/sentry_cli.cr -o ./bin/sentry
./bin/sentry -b "crystal build src/webapp.cr -o bin/webapp" -r bin/webapp
```
{% embed include file="src/examples/kemal/src/webapp.cr" %}



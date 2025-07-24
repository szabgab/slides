# Triggering jobs

* on

* [triggers](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)

* Single event

```
on: push
```

* Multiple events

```
on: [push, pull_request]
```

* Run on "push" in every branch.
* Run on "pull_request" if it was sent to the "dev" branch.
* scheduled every 5 minutes (cron config)

{% embed include file="src/examples/workflows/triggers.yml" %}

* Manual events (via POST request)



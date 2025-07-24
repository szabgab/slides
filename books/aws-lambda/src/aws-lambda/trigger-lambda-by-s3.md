# Trigger Lambda by S3


{% embed include file="src/examples/aws/s3_event.json" %}

Trigger by using:

```
aws s3 cp data.json s3://szabgab/new/data.json
```

Download the resulting file using

```
aws s3 cp s3://szabgab/out.json .
```



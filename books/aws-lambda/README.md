AWS Lambda ideas

What are policy templates?
   Basic Edge Lambda permissions

http://www.awslessons.com/2017/lambda-api-gateway-internal-server-error/

(also good Simple Microservice Permissions)


```
docker run -v $(pwd):/opt -it --rm aws
cd /opt
pip install editdistance -t pypi
```

find . -name "*.pyc" | xargs rm -f

See Dockerfile


Unable to import module 'lambda_function': libc.musl-x86_64.so.1: cannot open shared object file: No such file or directory

It is here /lib/libc.musl-x86_64.so.1 in the Alpine Docker image

[alpine linux](https://hub.docker.com/_/alpine/)

* [python-Levenshtein](https://pypi.org/project/python-Levenshtein/) is another module writte in C


## TODO
{id: todo}

* What is publish?

* Configure public hostname to access the API call.

* Set up database in AWS to hold our data.

* Cron / schedule an event.

* Send mail from AWS Lambda



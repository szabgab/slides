# AWS Lambda
{id: index}

## About us
{id: about-us}

* [Yonit Gruber-Hazani](https://www.linkedin.com/in/yonitgruber/)
* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

* [DevOps Workshops](http://devops-workshops.code-maven.com/)
* [Code Mavens Meetup](https://www.meetup.com/Code-Mavens/)

## What is Serverless?
{id: serverless}

* Function as a Service - FaaS

* 0 cost for deployment
* $ for usage
* No root access, just a simple function (or application)

## Create an AWS account
{id: create-account}

* [Create Free Account](https://aws.amazon.com/free/)
* You might need to supply a credit card, but AWS provides a Free tier.

## Start with AWS Lambda
{id: aws-lambda}

* [Visit AWS Lambda](https://aws.amazon.com/lambda/)
* Log in

* Region: us-east-1

## Task 1 - Hello World URL
{id: task-1}

* Create script in Python that can be accessesed via curl.

## Hello World in AWS Lambda
{id: hello-world}

* Press "Create function"

* Name: "hello"
* Runtime: Python 3.6
* Role: Create new role from template(s)
* Role name: "myrole"
* Policy templates: Basic Edge Lambda Permission
* Press "Create function"

The default code will look like this:

![](hello_world.py)

* Test it (click on "Test")
* First it will make you create a new test-case.

## Event Sources (Triggers)
{id: event-sources}

* [Supported Event Sources](https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html)
* Amazon API Gateway
* Scheduled Events
* Amazon S3
* Amazon DynamoDB
* Amazon Simple Email Service
* ...

## API Gateway
{id: api-gateway}

* "Add triggers" - select API Gateway
* Configure Required
* Create a new  API
* API name: demo
* Deployment stage: v0
* Security: Open

* Once we "save" it, we'll be able to see the "Invoke URL"
* https://s94rb025f9.execute-api.us-east-1.amazonaws.com/v0/hello

* curl ...


```
ERROR 502 Bad Gateway
```

or

```
{"message": "Internal server error"}
```

## Add header
{id: add-header}

* The function needs to return a dictionary with the status code and the headers.
* At least the Content-type.

![](hello_world_header.py)

* curl ...

## Send JSON
{id: send-json}

![](hello_world_json.py)

* curl ...

```
{"message": "Hello World!"}
```

## Event details
{id: event-details}

![](hello_world_json_event.py)

* curl ...

![](event.json)

## Exercise 1
{id: exercise-1}

* Create your own hello function.

## Task 2 - Accept URL GET parameters
{id: task-2}

* Accept parameter in the GET request and echo it back

## Accept Parameters
{id: accept-parameters}

![](echo.py)

* Save and Click "Test"
* Observe the error

```
{
  "errorMessage": "'queryStringParameters'",
  "errorType": "KeyError",
  "stackTrace": [
    [
      "/var/task/lambda_function.py",
      4,
      "lambda_handler",
      "name = event['queryStringParameters']['name']"
    ]
  ]
}
```

* Our Python code is not safe enough, we assume a field "name" to be passed in.

## Error via the API
{id: error-via-the-api}

* Before we fix the code, let's see what happens if we access the URL using `curl` ?

* curl ...

```
{"message": "Internal server error"}
```

* To see the error log, visit:

* Monitoring
* Invocation errors
* Jump to logs


## Test Event for API Gateway
{id: test-event-for-api-gateway}

* Before we fix the code, we can fix the test:

```
{
    "queryStringParameters" : {
        "name": "Foo Bar"
    }
}
```

* Try this using the "Test" button.

Also, try it from the console using `curl` or in your browser (use your own URL).

* curl 'https://qspmdah6oj.execute-api.us-east-1.amazonaws.com/v0/hello?name=Foo%20Bar'

```
{"message": "Hello Foo Bar!"}
```

## Exercise 2
{id: exercise-2}

* Fix the Python code so even if the user does not supply the "name" field it still won't crash.
* Instead make it return a JSON structure with status "400 Bad Request"
* Use `curl -I` or `curl -D err.txt` to check the headers as well.

* Create another function that will accept 2 numbers (parameters a and b) and add them together returning a JSON that looks like this:

```
{
   'a' : 23,
   'b' : 19,
   'op' : '+'
   'result' : 42
}
```

## Solution 2 - echo
{id: solution-2-echo}

![](echo_fixed.py)

## Solution 2 - add
{id: solution-2-add}

![](add_numbers.py)

## Task 3 - Multi file application
{id: task-3}

* Create an application that has more than one files.

## Multi-file application - json
{id: multi-file-application-json}

* Create a file called a.json with some JSON content in it.

![](a.json)

* Change the code to read the file and return it

![](read_json.py)

## Multi-file application - python module
{id: multi-file-application-module}

![](app1/lambda_function.py)

![](app1/mymod.py)

## Local development
{id: local-development}

```
mkdir project
cd project
vim lambda_function.py
```

![](app2/lambda_function.py)

```
zip ../project.zip *
```

* Upload a .ZIP file.
* Save.
* Try it using `curl`.

## Exercise 3
{id: exercise-3}

* Create a 'calculator' application that accepts two numbers 'a' and 'b' and an 'operation' that can be either 'add' or 'multiply'.
* Return the appropirate result.
* Create it on you computer in two files. A main web serving file and a module with two functions 'add' and 'multiply'

* On your local computer create a directory for a project.
* In the directory create a file called 'lambda_function.py' this will hold the main function.
* Create also a file called 'mymodule.py'.
* Upload the whole thing using zip.


## Solution 3
{id: solution-3-calc}

![](app3/lambda_function.py)

![](app3/mymodule.py)


## Task 4 - Use 3rd party Python modules.
{id: task-4}

* [Creating a Deployment Package for Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)


## Development machine
{id: development-machine}

* [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
* Using [pylev](https://pypi.org/project/pylev/) which is pure Python.


![](app_pylev/lambda_function.py)

```
mkdir app_pylev
cd app_pylev
pip install pylev -t pypi
zip -r ../project.zip *
```

* `curl 'https://qspmdah6oj.execute-api.us-east-1.amazonaws.com/v0/hello?a=abd&b=acx'`

## Error: must supply either home or prefix/exec-prefix — not both
{id: must-supply-either-home-or-prefix-exec-prefix-not-both}

On OSX you might get the above error. Create the 'setup.cfg' file.

![](app_pylev/setup.cfg)

## Third party not pure-python
{id: third-party-not-pure-python}

* [editdistance](https://github.com/aflc/editdistance) is a Levenshtein distance module written in C++ and Cython
* [See](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python)

![](app_editdistance/lambda_function.py)

![](app_editdistance/requirements.txt)

* Needs a linux box either locally or on Amazon AWS.

## Docker to build 3rd party modules
{id: docker-to-build}

[amazonlinux](https://hub.docker.com/_/amazonlinux/)

![](app/Dockerfile)

```
docker build -t aws .
```

* In the project directory:

```
docker run -v $(pwd):/opt  --rm aws pip install -r requirements.txt -t pypi
```

```
zip -r ../project.zip *
```

* Upload the zip file.

## Exercise 4
{id: exercise-4}

* Web Client: A function that uses 'requests' to fetch a URL and return the text of the page.

* A function that will accept the name of two cities.
* Call the API of [Open Weather Map](https://openweathermap.org/) and return the temprature difference in the two places.

## Solution: Web client
{id: web-client}

![](web_client/lambda_function.py)

![](web_client/requirements.txt)

![](web_client/setup.cfg)

```
pip install -r requirements.txt -t pypi
zip -r ../project.zip *
```

```
curl 'https://qspmdah6oj.execute-api.us-east-1.amazonaws.com/v0/hello?url=https://httpbin.org/get'
```

## Task 5 - Using S3 - Simple Storage Service
{id: s3-storage}

* Buckets - (all the users share a single name-space for buckets, so a lot of them are already taken)
* Create a bucket in [s3](https://s3.console.aws.amazon.com/s3) (eg. your-name)
* Add permission to the role [Attach policy](https://console.aws.amazon.com/iam/) AmazonS3FullAccess

* [boto 3](https://boto3.readthedocs.io/en/latest/)

## S3 List bucket
{id: list-s3-bucket}

![](list_s3_bucket.py)

## S3 write object from Lambda
{id: s3-write-object-from-lambda}

![](create_s3_object.py)

## Read S3 object
{id: read-s3-object}

![](read_s3_object.py)

## Trigger Lambda by S3
{id: trigger-lambda-by-s3}

![](s3_event.json)

Trigger by using:

```
aws s3 cp data.json s3://szabgab/new/data.json
```

Download the resulting file using

```
aws s3 cp s3://szabgab/out.json .
```

## Handle S3 event in Lambda
{id: handl-s3-event-in-lambda}

![](handle_s3_evetn.py)

## Exercise 5
{id: exercise-5}

* Create a function that can be triggered by a URL request passing in parameters like this: ?name="Foo Bar"
* Create an object in S3 called something like "in/time.json"  (with the current time)

* Create another function that will be triggered by a newaobject  with a perfix "in/"
* Load that object and creare a new object called "out/time.json" using the same object name, but adding 3 new fields to it called

```
new_time:  the time portion of the name of the object
end_time:  the time when we read the object in the second function.
elapsed:   the difference.
```

## TODO
{id: todo}

* What is publish?

* Configure public hostname to access the API call.

* Set up database in AWS to hold our data.

* Cron / schedule an event.

* Send mail from AWS Lambda

## AWS Resources
{id: aws-resources}

* [Serverless Developer Tools](https://aws.amazon.com/serverless/developer-tools/)

## Resources
{id: resources}


* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)


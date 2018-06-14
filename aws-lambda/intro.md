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

## Hello World in AWS Lambda
{id: hello-world}

* Create sample script in Python that can be accessesed via curl, get parameter, return it.

* Press "Create function"

* Name: "myhello"
* Runtime: Python 3.6
* Role: Create new role from template(s)
* Role name: "myrole"
* Policy templates: Simple Microservice Permissions

The default code will look like this:

![](hello_world.py)

* Test it (click on "Test")
* First it will make you create a new test-case.

## API Gateway
{id: api-gateway}

* "Add triggers" - select API Gateway
* Configure Required
* Create a new  API
* API name: trymyhello
* Deployment stage: anything
* Security: Open

* Once we "save" it, we'll be able to see the "Invoke URL"
* https://s94rb025f9.execute-api.us-east-1.amazonaws.com/anything/myhello

* curl ...

```
ERROR 502 Bad Gateway
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

curl https://nck2wezqxl.execute-api.us-east-1.amazonaws.com/demo/hello

curl - Internal Server Error

![](hello_world_json_public.py)

## Accept Parameters
{id: accept-parameters}

![](echo.py)

## Multi-file application
{id: multi-file-application}

* Create a file called a.json with some JSON content in it.

![](a.json)

* Change the code to read the file and return it

![](read_json.py)

![](read_json_param.py)

## Deployment
{id: deployment}

```
mkdir project
cd project
vim hello_world.py
zip ../project.zip *
```

![](app1/hello_world.py)

![](app1/hello_world.py)

![](app/lambda_function.py)

## Public URL
{id: public-url}

* Configure public hostname to access the API call.


## TODO
{id: todo}


* An application using a module that is not available in Lambda. (Installing modules)

* A function that will accept the name of two cities, call the https://openweathermap.org/ and return the temprature difference in the two places.

* Set up some database in AWS to hold our data.

* Cron / schedule an event.

* Send mail from AWS Lambda


## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)


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

* Function as a Service FaaS

## Plan
{id: plan}


* An application using a module that is not available in Lambda. (Installing modules)

* A function that will accept the name of two cities, call the https://openweathermap.org/ and return the temprature difference in the two places.

* Set up some database in AWS to hold our data.

* Cron / schedule an event.

* Send mail from AWS Lambda

## Create an AWS account
{id: create-account}

## Hello World in AWS Lambda
{id: hello-world}

* Create sample script in Python that can be accessesed via curl, get parameter, return it.

[](hello_world.py)

* Test it

[](hello_world_json.py)

curl https://nck2wezqxl.execute-api.us-east-1.amazonaws.com/demo/hello

curl - Internal Server Error

[](hello_world_json_public.py)

[](echo.py)


## Multi-file application
{id: multi-file-application}

* Create a file called a.json with some JSON content in it.

[](a.json)

* Change the code to read the file and return it

[](read_json.py)

[](read_json_param.py)

## Deployment
{id: deployment}

```
mkdir project
cd project
vim hello_world.py
zip ../project.zip *
```



## Public URL
{id: public-url}

* Configure public hostname to access the API call.



## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)




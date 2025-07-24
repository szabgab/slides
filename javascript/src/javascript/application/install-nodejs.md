# Install NodeJS


* [NodeJS](https://nodejs.org/)   (There is 18.16.0 LTS and Installing 20.3.0 Current)

* Create a folder for the application, eg. examples/demo-app
* Open CMD , cd to the folder of the application `cd examples/demo-app`
* Create project `npm init -y`  (The -y will make it use the defaults withot prompting for answers)


* [Install webpack](https://webpack.js.org/guides/installation) by running `npm install --save-dev webpack webpack-cli`
* These will install it in the `node_modules` folder and it will also create the files `package.json` and `package-lock.json`

Edit the package.json and add

```
  "scripts": {
    "build": "webpack --mode development",
    "watch": "webpack --mode development --watch"
  }
```

Then running

```npm run build```



{% embed include file="src/examples/demo-app/dist/index.html" %}
{% embed include file="src/examples/demo-app/src/index.js" %}
{% embed include file="src/examples/demo-app/src/mymath.js" %}

{% embed include file="src/examples/demo-app/package.json" %}

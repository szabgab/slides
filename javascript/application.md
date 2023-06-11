# Application
{id: application}

## Install NodeJS
{id: install-nodejs}


* [NodeJS](https://nodejs.org/)   (There is 18.16.0 LTS and Installing 20.3.0 Current)

* Create a folder for the application, eg. examples/demo-app
* Open CMD , cd to the folder of the application `cd examples/demo-app`
* Create project `npm init -y`  (The -y will make it use the defaults withot prompting for answers)


* [Install webpack](https://webpack.js.org/guides/installation) by running `npm install --save-dev webpack webpack-cli`
* These will install it in the `node_modules` folder and it will also create the files `package.json` and `package-lock.json`

Edit the package.json and add

```
  "scripts": {
    "build": "webpack --config webpack.config.js"
  }
```

Then running

```npm run build```



![](demo-app/dist/index.html)
![](demo-app/src/index.js)
![](demo-app/src/mymath.js)

![](demo-app/package.json)
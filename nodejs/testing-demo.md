# Testing Demo for NodeJS projects
{id: testing-demo}


## Testing Demo to Application Under Test
{id: testing-demo-aut}

![](examples/testing-demo/mycalc.js)


## Using the JavaScript library
{id: testing-demo-using-the-library}

![](examples/testing-demo/add.js)

```
node add.js
```

## Testing Demo with Mocha
{id: testing-demo-with-mocha}

npm init -y
npm install mocha
npm install mocha-cli

* [mocha](https://mochajs.org/)

![](examples/testing-demo/package.json)

![](examples/testing-demo/package-lock.json)


## Testing Demo with Mocha success
{id: testing-demo-mocha-success}

![](examples/testing-demo/test/first.js)

```
./node_modules/mocha/bin/mocha.js test/first.js 
```

## Testing Demo with Mocha failure
{id: testing-demo-mocha-failure}

![](examples/testing-demo/test/several.js)


```
./node_modules/mocha/bin/mocha.js test/several.js 
```

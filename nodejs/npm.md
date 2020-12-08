# npm
{id: npm}

## npmjs
{id: npmjs}


* [npm](https://www.npmjs.com/)
* Private npm repository in the cloud: https://gemfury.com/

## npm init
{id: npm-init}

* Create a directory for the project (eg. mynode) and cd into the directory

```
npm init
```

This will aske a few questions and create the package.json file.

The questions, and the default answers, you can just accept the defaults.

```
package name: mynode
version: 1.0.0
description:
entry point: index.js
test command:
git repository:
keywords:
author:
license (ISC):
```

```
npm init --yes
```

* Would populate the file with the defaults without asking emberassing questions.


## package json
{id: package-json}

![](examples/manual/package.json)

## npm install PACKAGE
{id: npm-install-package}


```
npm install module
npm uninstall module
```

* This will install in the `node_modules` folder in the directory where the package.json can be found
* And it will add the name of the package to packege.json as well declaring it as a dependency
* It will also create a file called `package-lock.json`.
* Both json files should be added to git and the node_modules/ directory should be added to gitignore

## Development dependencies
{id: development-dependencies}

```
npm install mocha --save-dev
```

* It is added to the `devDependencies` section in the package.json file


## Semanic Versioning
{id: semantic-versionins}

* [About Semantic Versioning](https://docs.npmjs.com/about-semantic-versioning)
* [Semantic version calculator](https://semver.npmjs.com/)

```
^1.2.3   means 1.x.x
~1.2.3  means  1.2.x
1.2.3   exact version number
```

## npm install
{id: npm-install}

* Based on `pacakge.json` and `package-lock.json` this will install all the depdendencies.
* Useful to recreate the environment.

```
npm install
```


## npx
{id: npx}

* [npx](https://www.npmjs.com/package/npx)
* [Introducing npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b)


## Linter - ESLint
{id: linter}

* [ESLint](https://eslint.org/)

```
npm install eslint --save-dev
npx eslint --init
```

Creates:

```
.eslintrc.json
```

![](examples/basic/.eslintrc.json)

* Set the [rules](https://eslint.org/docs/rules/)

Run it:

```
npx eslint *.js
```

In `package.json` set:

```
  "scripts": {
    "test": "npx eslint *.js"
  },
```

Then run as

```
$ npm run test
```


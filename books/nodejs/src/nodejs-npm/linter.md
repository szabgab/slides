# Linter - ESLint

* [ESLint](https://eslint.org/)

```
npm install eslint --save-dev
npx eslint --init
```

Creates:

```
.eslintrc.json
```

{% embed include file="src/examples/basic/.eslintrc.json)

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



# SVG validation


## xmllint (part of libxml2)

```
sudo apt install libxml2-utils
```

```
xmllint --noout yourfile.svg
```

prints nothing and sets exit  code to 0 on success

print error message and sets exit code to non-0 on failure

Check XML validity, but not specific to SVG.

One could use the SVG DTD.

## svglint (Node.js-based)

SVG-specific linting beyond just XML structure. Requires node.js

```
npm install -g svglint
```

```
svglint yourfile.svg
```


## svgcheck (Python script)

Checking if an SVG file follows the SVG spec more closely.

Install:

```
pip install svgcheck
```

Usage:

```
svgcheck yourfile.svg
```


## W3C Validator (Local via Docker)

The W3C Markup Validator can be run locally via Docker for comprehensive validation.

```
docker run -v $(pwd):/var/www:ro validator/validator /var/www/yourfile.svg
```



# GitHub Pages
{id: github-pages}

## Setting up GitHub page
{id: setting-up-github-page}

* Create an account on [GitHub](https://github.com/)
* Create a GitHub repository called USERNAME.github.io
* Create a file called **index.html**
* Visit https://USERNAME.github.io (it may take a few minutes to update)
* For GitHub Organizations it is exactly the same process.

![](examples/index.html)


## GitHub page with Jekyll
{id: github-page-with-jekyll}

* [Jekyll](https://jekyllrb.com/) a static site generator
* [Markdown](https://daringfireball.net/projects/markdown/)
* [GitHub flavored Markdow](https://guides.github.com/features/mastering-markdown/)
* Create a file called **about.md**
* Visit https://USERNAME.github.io/about
* Note: the .html files take precedence over the .md files!

![](examples/about.md)


## Jekyll themese
{id: jekyll-themes}

* [themes](https://pages.github.com/themes/)
* Create **_config.yml** with **theme: jekyll-theme-cayman**



## Themes layout
{id: theme-layout}

* [themes](https://pages.github.com/themes/)
* [Cayman in GitHub](https://github.com/pages-themes/cayman)
* [Cayman demo](https://pages-themes.github.io/cayman/)
* [_layouts/default.html](https://github.com/pages-themes/cayman/blob/master/_layouts/default.html) look at the template tags to learn about config options.



## Site-wise configuration
{id: site-wise-configuration}

* In **_config.yml**

![](examples/_config.yml)



## Page-specific configuration - frontmatter
{id: page-specific-configuration}

* At the top of the .md files
* [Frontmatter documentation](https://jekyllrb.com/docs/frontmatter/)


```
---
title: About the szabgab page
---
```


## JavaScript code
{id: javascript-code}

![](examples/js.md)

* One can include plain HTML in the md file. So include **script** tags.
* The code should come at the end to have the DOM available already.



## Load jQuery and add jQuery code
{id: load-jquery-code}

![](examples/jquery.md)
![](examples/demo.js)

When you change the JavaScript file, make sure it is reloaded! Browser cashing can cause you a bad day.



## Add a JSON file, load it with jQuery and display the content
{id: load-json-file}

![](examples/json.md)
![](examples/json.js)
![](examples/data.json)



## Other
{id: other}



In the _config file we can add a field called **description:**. It will provide the content for the subtitle of the header.



```
description: Some text
```





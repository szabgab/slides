# GitHub Pages
{id: github-pages}

## Why use version control?
{id: why-use-version-control}

* Everyone uses some version control. (e.g. by copying the document with a date suffix).
* There are many version control systems (VCSs).
* `git` is the de-facto standard these days. It is open source and free. It is integrated in many tools.
* [GitHub](https://github.com/) is the most popular cloud-based hosting service for `git` repositories with many extra features.

## GitHub Account
{id: github-account}

* If you don't have an account yet on [GitHub](https://github.com/) then create one now.
* It should be personal. It will remain with you for your life. (or the life of GitHub)
* It should not be related to your current educational institute or workplace or this presentation or course.

* My account is [szabgab on GitHub](https://github.com/szabgab/). It is my nickname almost everywhere on the Internet.

## GitHub Avatar
{id: github-avatar}

* Add a picture or an avatar of you to make your account more recognizable.
* Your profile / Edit profile / ...

## Setting up GitHub page
{id: setting-up-github-page}

* Create a GitHub repository called USERNAME.github.io (using your own USERNAME).
* For user [szabgab](https://github.com/szabgab/) it is [szabgab.github.io](https://github.com/szabgab/szabgab.github.io).
* Make the new repository public so we'll all be able to see the source.
* Check the "Add a README file" checkbox.

* Check the `Actions` tab to see the process generating the web site.

* Visit https://USERNAME.github.io (it may take a few minutes to update)
* For user szabgab it is [szabgab.github.io](https://szabgab.github.io/).
* For GitHub Organizations it is exactly the same process.

## GitHub page with Jekyll
{id: github-page-with-jekyll}

* [Jekyll](https://jekyllrb.com/) a static site generator

## Makrdown
{id: markdown-links}

* [Markdown](https://daringfireball.net/projects/markdown/)
* [GitHub flavored Markdow](https://github.github.com/gfm/)


## Markdown
{id: markdown}

* Titles: One or more `#` followed by the the title
* **Bold** `**` on both sides
* _Italic_ `_` on both sides

* Horizontal separator `---`.

* Link to some other site. e.g. to the slides.

* Unordered list. `*`
* Ordered list (both with ordered numbers and with  `1.`-s)

* Add image from other site `![](http://www.adelaidezoo.com.au/wp-content/uploads/sites/2/2016/03/Fu-Ni-7.jpg)`
* Upload an image and show it. `![my ant](little-black-ants.jpg)`

* Table

* Verbatim with backticks.
* Inline with one-tick.
* Multiline with 3-ticks. Add also programming language for highlighting.
* Indenting 4 spaces also works.


## Add page
{id: add-another-page}

* Create a file called `about.md`.
* Visit https://USERNAME.github.io/about
* Show how to linke to it from the main page.

![](examples/about.md)


## Customized 404 Page not found
{id: page-not-found}

Create the `404.md` files.


## Jekyll themese
{id: jekyll-themes}

* [themes](https://pages.github.com/themes/)
* Create `_config.yml` with `theme: jekyll-theme-cayman`


## Themes layout
{id: theme-layout}

* [themes](https://pages.github.com/themes/)
* [Cayman in GitHub](https://github.com/pages-themes/cayman)
* [Cayman demo](https://pages-themes.github.io/cayman/)
* [_layouts/default.html](https://github.com/pages-themes/cayman/blob/master/_layouts/default.html) look at the template tags to learn about config options.


## Site-wise configuration
{id: site-wise-configuration}

* In `_config.yml`

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

* One can include plain HTML in the md file. So include `script` tags.
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



In the _config file we can add a field called `description:`. It will provide the content for the subtitle of the header.

```
description: Some text
```

* Create a file called **index.html**

![](examples/index.html)

* Note: the .html files take precedence over the .md files!


## Examples
{id: examples}


* [rustatic](https://rustatic.code-maven.com/) - [source](https://github.com/szabgab/rustatic/) using Jekyll.
* my simple site [github.szabgab.com](https://github.szabgab.com/) - [soruce](https://github.com/szabgab/real-szabgab.github.io) using only Markdown files and the default Jekyll processor on GitHub pages.
* [Kantoniko](https://kantoniko.com/) - [source](https://github.com/kantoniko/) - using Python combining data from many repositories.  A dictionary and content in Ladino. Written in Python collecting data from multiple repositories.
* my personal site [szabgab.com](https://szabgab.com/) - [source](https://github.com/szabgab/szabgab.com) - using Perl.
* [Perl Weekly](https://perlweekly.com/) - [source](https://github.com/szabgab/perlweekly) - Perl, generate the site locally and push the HTML files as well.

* The students of [WIS Python course started in 2024-04](https://github.com/szabgab/wis-python-course-2024-04)
* The students of [WIS Python course started in 2024-11](https://github.com/szabgab/wis-python-course-2024-11)


* [Jekyll](https://jekyllrb.com/) a static site generator.
* Many [Static Site Generators](https://jamstack.org/generators/).

* [Planet Perl](https://perl.theplanetarium.org/) - [source](https://github.com/PerlToolsTeam/planetperl) using Perl.
* [Forem Reports](https://forem.code-maven.com/) - [source](https://github.com/szabgab/forem-reports).
* [(Rust) virtual events](https://events.code-maven.com/) - [source](https://github.com/szabgab/virtual-events).
* [Ruby Digger](https://ruby-digger.code-maven.com/) - [source](https://github.com/szabgab/ruby-digger)
* CPAN Digger

* [Rust Maven](https://rust.code-maven.com/) - [source](https://github.com/szabgab/rust.code-maven.com/) - [Rust Maven SSG](https://ssg.code-maven.com/) written in Rust.
* [Rust news](https://rust-news.code-maven.com/) written in Rust, collectin RSS/Atom feeds and generating the web site.

* Code Maven sites
* Perl Maven sites

* [slides](https://slides.code-maven.com/) - [source](https://github.com/szabgab/slides/) - [generator](https://github.com/szabgab/slider-py) written in Python.

* [rust.org.il](https://rust.org.il/) - [source](https://github.com/szabgab/rust.org.il/) written in Rust.
* [python.org.il](https://python.org.il/) - [source](https://gitlab.com/hamakor/python.org.il/) is written in Python but it is hosted on GitLab pages.

## Rename repository
{id: rename-repository}

* Rename repository so I'll be able to demo this later as well.
* Show how to access the web site now.

## Open Issue
{id: open-issue}

* Show how to open an issue on the repository with a link to your site and repository.
* Show with my own site.

## Add table of people
{id: add-table-of-people}

* Take the data from the issue and add it to the table listing the web sites.


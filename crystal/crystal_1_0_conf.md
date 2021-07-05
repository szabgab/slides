# Crystal from 0 to Web site
{id: crystal-from-0-to-web-site}

## Crystal from 0 to Web site
{id: crystal-1-0-title}

* Crystal 1.0 Conference
* 2021.07.08
* by Gábor Szabó

## Background
{id: crystal-1-0-conf-background}

* Programming 40 years.
* Perl 25 years
* Python 10 years
* Crystal 30 days

{aside}
actually it is already almost 60 days)
{/aside}

## Why?
{id: crystal-1-0-conf-why}

* [modulecounts](http://www.modulecounts.com/)
* [3rd party registry](https://code-maven.com/package-registry)
* Listing shards [crystalshards.xyz](https://crystalshards.xyz/)

{aside}
This site listing the shards are very plain, only a thin wrapper around GitHub API
I can do a much better one analyzing shards and displaying information.
{/aside}

## I can do better
{id: i-can-do-better}

* [Meta::CPAN](https://metacpan.org/)
* [PyDigger](https://pydigger.com/)

## How to learn
{id: crystal-1-0-conf-how-to-learn}

* Prepare slides for a [training course](https://code-maven.com/crystal-course)
* Developing an application

{aside}
Lots of small examples, questions arise, make me learn more.
{/aside}

## When
{id: crystal-1-0-conf-when}

* Sat May 15 13:48:30 2021 +0300 - first commit to [slides](https://code-maven.com/slides/crystal/)

* Wed May 19 07:29:28 2021 +0300 - first commit to [Crystal Mine](https://crystal-mine.org/)

* Wed Jun  9 03:03:02 2021 +0300 - posted on the [forum](https://forum.crystal-lang.org/)

* 4 hours later Johannes Müller pointed to [Shardbox](https://shardbox.org/)

## What did I learn?
{id: crystal-1-0-conf-what-did-i-learn}

* Crystal
* Web development with Crystal

## Crystal is fun
{id: crystal-1-0-conf-crystal-is-fun}

* Nice syntax
* Lots of methods
* Not a small language

## Shards install dependency issues
{id: crystal-1-0-conf-shards-install-issues}

`shards install`

Failed to resolve dependencies, try updating incompatible shards or use --ignore-crystal-version as a workaround if no update is available.

## What do ? and ! mean?!
{id: crystal-1-0-conf-what-do-these-mean}

* What does ? mean
* What does ! mean
* What if they are both: `!var.empty?`

{aside}
What to ? and ! mean at the end of the functions and sometimes at the end of various statements?
What does !something.empty? and why don't you write ¡empty! anyway? That would at least make sense...
{/aside}


## More Unicode characters
{id: crystal-1-0-conf-inverted}

* Why are we not using ¡ and ¿

## Meaning of ?
{id: crystal-1-0-conf-question-mark}

* `var.nil?`   - true/false
* `array[42]?` - nil instead of exception
* `String?`    - `String | Nil`

* But `answer?` can return 42

## Meaning of !
{id: crystal-1-0-conf-exclamation-mark}

* There is `p`.
* There is `p!` that is like `p`, but more so.

* Hash#reject  - returns a hash without some elements
* Hash#reject! - does it in-place

* Hash#delete - removes an element in-place

{aside}
It seems there is some inconsitency here.
{/aside}



## Web framework?
{id: crystal-1-0-conf-web-framework}

* Are there any frameworks?
* Which framework to use?
* [crystal-web-framework-stars](https://github.com/isaced/crystal-web-framework-stars)

* [Amber](https://amberframework.org/)
* [Kemal](https://kemalcr.com/)
* [Lucky](https://luckyframework.org/)

## Amber Framework
{id: crystal-1-0-conf-amber}

* Complex installation (starts by installing Crystal?)

```
curl -L https://github.com/amberframework/amber/archive/stable.tar.gz | tar xz
cd amber-stable
shards install
make install
```

* It wants to install in `/usr/local/bin/amber` why?
* There is some talk about docker-compose...

## Lucky Framework
{id: crystal-1-0-conf-lucky}

* Installation is complex
* Needs PostgreSQL on my development machine?
* A docker-compose up would be great.

## Kemal
{id: crystal-1-0-conf-kemal}

* The simplest to get started
* Might not be as powerful as the others
* Most popular of the 3

![](examples/crystal-1-0-conf/shard.yml)

## GitHub Actions
{id: crystal-1-0-conf-github-actions}

[GitHub Actions configurator](https://crystal-lang.github.io/install-crystal/configurator.html)

The need to recompile the whole thing before I run it and the fact that compilation is slow makes life of a (web) developer hard.

## Crinja
{id: crystal-1-0-conf-crinja}

* The Jinja Template system of Johannes Müller
* No need for compilation - makes the HTML development much faster.

## Code formatter
{id: crystal-1-0-conf-format-code}

```
crystal tool format
```

## Ameba
{id: crystal-1-0-conf-ameba-linter}

[Ameba Linter](https://github.com/crystal-ameba/ameba)

## Shardbox
{id: crystal-1-0-conf-shardbox}

* [Shardbox](https://shardbox.org/)

* Kemal
* Crinja (templates)
* PostgreSQL


## Pro and contra
{id: crystal-1-0-conf-pro-and-contra}

* Many common libraries are missing - harder to develop and many opportunities


## Future
{id: crystal-1-0-conf-future}

* [Shardbox](https://shardbox.org/)

* [Crystal Weekly](https://crystalweekly.com/) by Serdar Doğruyol
* [Friends of Crystal](https://friendsofcrystal.com/) by Serdar Doğruyol
* [Crystal course](https://code-maven.com/crystal-course)
* Crystal book (based on the course)


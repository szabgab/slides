# Crystal from 0 to Web site
{id: crystal-from-0-to-web-site}

## Crystal from 0 to Web site
{id: crystal-1-0-title}

* Crystal 1.0 Conference
* 2021.07.08
* by Gábor Szabó
* https://szabgab.com/
* https://code-maven.com/crystal
* @szabgab

## Background
{id: crystal-1-0-conf-background}

* Programming 40 years.
* Perl 25 years.
* Python 10 years.
* Crystal 30 days.

* Teaching programming for 20 years.
* Test automation / CI / DevOps

{aside}
Actually it is already almost 60 days
{/aside}

## Why?
{id: crystal-1-0-conf-why}

* [module counts](http://www.modulecounts.com/)
* [3rd party registry](https://code-maven.com/package-registry)
* Listing of shards [crystalshards.xyz](https://crystalshards.xyz/) (thin wrapper around the API of GitHub)

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

* Developing an application
* Prepare slides for a [training course](https://code-maven.com/crystal-course)

{aside}
Lots of small examples, questions arise, make me learn more.
{/aside}

## When
{id: crystal-1-0-conf-when}

* Sat May 15 13:48:30 2021 +0300 - first commit to [slides](https://code-maven.com/slides/crystal/)

* Wed May 19 07:29:28 2021 +0300 - first commit to [Crystal Mine](https://crystal-mine.org/)

* Wed Jun  9 03:03:02 2021 +0300 - posted on the [Crystal forum](https://forum.crystal-lang.org/)

## Shardbox
{id: crystal-1-0-conf-4-hours}

* 4 hours later Johannes Müller pointed to [Shardbox](https://shardbox.org/)

## What did I learn?
{id: crystal-1-0-conf-what-did-i-learn}

* Crystal
* Web development with Crystal

## Crystal is fun
{id: crystal-1-0-conf-crystal-is-fun}

* Nice syntax
* "Make the easy things easy, hards things possible"
* Tim Toady - TMTOWTDI - "There's more than one way to do it"
* Lots of methods
* Not a small language

## Shards
{id: crystal-1-0-conf-shards}

* Easy to install (`shards install`).
* Few of them. Many common libraries (shards) are missing - harder to develop and many opportunities.
* Discover-ability (There is no `shards search`, there is no central database of shards).
* "Failed to resolve dependencies, try updating incompatible shards or use `--ignore-crystal-version` as a workaround if no update is available."

## Code formatter
{id: crystal-1-0-conf-format-code}

```
crystal tool format
```

## Ameba - Linter
{id: crystal-1-0-conf-ameba-linter}

* [Ameba Linter](https://github.com/crystal-ameba/ameba)

## Spectator - testing framework
{id: crystal-1-0-conf-spectator}

* [Spectator](https://gitlab.com/arctic-fox/spectator) (similar to RSpec of Ruby)

## Code coverage
{id: crystal-1-0-conf-code-coverage}

* [Crystal - code coverage](https://github.com/anykeyh/crystal-coverage)

## CI - GitHub Actions
{id: crystal-1-0-conf-github-actions}

* [GitHub Actions configurator](https://crystal-lang.github.io/install-crystal/configurator.html)
* Smoking Crystal and the shards

## The language
{id: crystal-1-0-conf-the-language}

## What do ? and ! mean?!
{id: crystal-1-0-conf-what-do-these-mean}

* What does ? mean
* What does ! mean
* What if they are both: `!var.empty?`

{aside}
What to ? and ! mean at the end of the functions and sometimes at the end of various statements?
What does !something.empty? and why don't you write ¡empty! anyway? That would at least make sense...
{/aside}


## Emojis and Unicode characters 💎
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
It seems there is some inconsistency here.
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

* The need to recompile the whole thing before I run it and the fact that compilation is slow makes life of a (web) developer hard.

![](examples/crystal-1-0-conf/shard.yml)

## Crinja
{id: crystal-1-0-conf-crinja}

* The Jinja Template system of Johannes Müller
* No need for compilation - makes the HTML development much faster.

## Shardbox
{id: crystal-1-0-conf-shardbox}

* [Shardbox](https://shardbox.org/)

* Kemal
* Crinja (templates)
* PostgreSQL


## Future
{id: crystal-1-0-conf-future}

* Contribute to [Shardbox](https://shardbox.org/)
* Contribute to shards. (tests, CI)
* [Pair programming sessions](https://code-maven.com/live) on Crystal projects

* [Crystal course](https://code-maven.com/crystal-course)
* Crystal book (based on the course)

## Thank you - QA ?!?!
{id: crystal-1-0-conf-thank-you}

* Thank you - QA
* https://szabgab.com/
* https://code-maven.com/crystal
* [Discord](https://discord.com/channels/591460182777790474/851915558970064937)
* @szabgab


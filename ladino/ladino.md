# Ladino
{id: ladino}

## The dictionary
{id: the-dictionary}

* [Dictionary](https://diksionaryo.szabgab.com/)

## About Ladino
{id: about-ladino}

* Ladino
* Judeo-Espanyol
* Judeo-Spanish
* Judezmo
* Espanyol (our spanish)

* Haketia (in Marokko)

## Origin of Ladino
{id: origin-of-ladino}

* Romance language based on old Spanish and a lot of other languages:

* Castillian Spanish
* Portugueses
* Aragonese
* Catalan
* Italian
* French
* Turkish
* Greek
* Bulgarian
* Serbo-Croatic
* Arabic
* Hebrew
* ...

## Expulsion of Sefardic Jews
{id: expulsion-of-sefardic-jews}

* 1492 from Spain
* 1496 from Portugal as well

* Spread to a lot of places in Western Europe, North Africa and the Ottoman Empire

* [some maps](https://duckduckgo.com/?q=map+of+expulsion+of+jews+from+spain&t=ffab&iar=images&iax=images&ia=images)

## Writing system
{id: writing-system}

* Latin letters
* Rashi script
* Solitreo

* See [Ladinotype](https://ladinotype.com/)

## Who am I and how I learned Ladino
{id: who-am-i}

* Gabor Szabo
* Programmer (test automation, DevOps)
* Hungary => Israel
* Learning modern Spanish for 3.5 years. (Duolingo, italki, eBooks, podcasts, youtube videos)
* Learning Ladino for 6 months.


## Goals
{id: goals}

* Be able to communicate with other Ladino speaker.
* Help others in the same goal.
* Help preserve the language and the culture.


## My site about Ladino
{id: site-about-ladino}

* [Ladino](https://ladino.szabgab.com/)

## LibreLingo
{id: libre-lingo}

* [LibreLingo](https://librelingo.app/)

## LibreTranslate
{id: libre-translate}

* [LibreTranslate](https://libretranslate.com/)
* Needs a huge corpus of text in two languages.

## Ladino communities
{id: ladino-communities}

* [Ladinokomunita](https://ladinokomunita.groups.io/)
* [Ladinadores](https://www.facebook.com/groups/ladinadores)


* [Facebook](https://ladino.szabgab.com/en/ladino-on-facebook)


## Ladino academy
{id: ladino-academy}

* [Ladino academy](https://autoridadnasionala.wixsite.com/autoridadnasionala/copia-de-%D7%94%D7%90%D7%A7%D7%93%D7%9E%D7%99%D7%94-%D7%94%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99%D7%AA-%D7%9C%D7%9C%D7%90%D7%93%D7%99%D7%A0%D7%95) (2018)

## Existing Ladino dictionaries
{id: ladino-dictionaries}

* [dictionaries](https://ladino.szabgab.com/en/ladino-dictionaries)

## The dictionary
{id: the-online-dictionary}

* [Dictionary](https://diksionaryo.szabgab.com/)

## Quick overview of the technology
{id: quick-overview}


* [data](https://github.com/szabgab/ladino-diksionaryo-data/) -  YAML files
* [whatsapp](https://github.com/szabgab/ladino-estamos-whatsapeando/) - YAML and ogg files
* [sounds](https://github.com/szabgab/ladino-diksionaryo-sounds/) - ogg files

* [code](https://github.com/szabgab/ladino-diksionaryo-code/) - [Python](https://www.python.org/), [JQuery](https://jquery.com/), [Bulma](https://bulma.io/)

* [generated](https://github.com/szabgab/ladino-diksionaryo-generated/) - GitHub Action

## The source of the dictionary
{id: source-of-the-dictionary}

* Source Excel file Created by Güler Orgun, Ricardo Portal i Antonio Ruiz Tinoco 2003-2009
* Contributed to Ladinokomunita
* Converted to YAML files automatically and then manual cleanup

## YAML representation
{id: yaml-representation}

* Different spellings of the same word
* Different words for the same thing (e.g. in different locations)

* Gender
* Singular/plural

* Conjugation of verbs (regular, irregular) (we have 600 verbs now)

## config.yaml
{id: config-yaml}

* categories
* acceptable values of certain fields (origines, grammar, gender, etc.)
* lists of words
* list of extra pages (in markdown format)

## Processing in Python
{id: processing-in-python}

* Read the config file and all the YAML files.
* Verify what that the fields have correct values (from the list of valid values)
* Verify certain other things.

* Generate HTML files for each word
* Generate JSON files to be used by the front-end.
* Generate some extra files

## CI/CD
{id: ci-cd}

* Pushing to any of the repositories will run some local test.
* Trigger the action of the "generated" repo.
* gitHub pages gets updated.

## Front-end
{id: front-end}

* JQuery
* The main page only (and the Konfig and the Game)


## Tests for the code
{id: tests-for-the-code}

* Using a few real words.
* Using a few YAML files with specific issues.
* Comparing the results to the previous runs.


## Issues to handle
{id: issues-to-handle}

* Conjugations of verbs
* Multi-word expressions? "me ambezo"
* Connection between words (e.g. plural of ..., conjugation of ...)
* Dictionary is getting big (1 Mb)

* Make it easy for people to suggest changes?!


## Questions
{id: question}

* Which words to include? (today: enlase, atadijo, link)
* Which spelling(s) to include? (dia, diya) (djueves, djugeves, djugueves)
* Which one(s) to recognize and which ones to recommend?

* When is a word "part of the language"?

## QA session
{id: qa-session}

* Thank you - Questions?



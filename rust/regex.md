# Regex
{id: regex}


## Regex match exact text
{id: regex-match-exact-text}
{i: Regex}
{i: captures}

* [regex::Captures](https://docs.rs/regex/latest/regex/struct.Captures.html)

![](examples/regex-simple-match/Cargo.toml)

![](examples/regex-simple-match/src/main.rs)


```
The black cat climbed the green tree
Full match: 'cat'
No match
```


## Regex match numbers - capture using parentheses
{id: regex-match-numbers}
{i: Regex}
{i: captures}
{i: (}
{i: )}

* [regex::Captures](https://docs.rs/regex/latest/regex/struct.Captures.html)

![](examples/regex-demo/src/main.rs)

## Regex capture all the numbers - multiple match
{id: regex-capture-all-the-numbers}
{i: Captures}
{i: captures_iter}

* [regex::Captures](https://docs.rs/regex/latest/regex/struct.Captures.html)

![](examples/regex-capture-multiple-numbers/src/main.rs)

```
There is the number 23 and another number here: 19
23
19
["23", "19"]
```


## Regex
{id: regex-substitute}
{i: Captures}
{i: replace}
{i: repalce_all}

![](examples/regex-substitute/Cargo.toml)
![](examples/regex-substitute/src/main.rs)


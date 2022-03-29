# Regular Expressions - part 2
{id: regex-2}


## Optional character
{id: regex-optional}
{i: ?}

Match the word **color** or the word **colour**

```
Regex: r'colou?r'
```

```
Input: color
Input: colour
Input: colouur
```


## Regex match 0 or more (the * quantifier)
{id: regex-quantifiers}
{i: *}

Any line with two - -es with anything in between.

```
Regex: r'-.*-'
Input: "ab"
Input: "ab - cde"
Input: "ab - qqqrq -"
Input: "ab -- cde"
Input: "--"
```


## Quantifiers
{id: quantifiers}
{i: quantifiers}
{i: ?}
{i: +}
{i: *}


Quantifiers apply to the thing immediately to the left of them.

In this case it is the single character `x` to the left of the quantifier, but later we'll see it can apply to a character-class or to a sub-expression enclosed in parentheses as well.
Whatever is located immediately to the left of the quantifier.



```
r'ax*a'      # aa, axa, axxa, axxxa, ...
r'ax+a'      #     axa, axxa, axxxa, ...
r'ax?a'      # aa, axa
r'ax{2,4}a'  #          axxa, axxxa, axxxxa
r'ax{3,}a'   #                axxxa, axxxxa, ...
r'ax{17}a'   #                                 axxxxxxxxxxxxxxxxxa
```
|  *  |  0-   |
|  +  |  1-   |
|  ?  |  0-1  |
|  {n,m}  |  n-m  |
|  {n,}  |  n-  |
|  {n}  |  n  |


## Quantifiers limit
{id: quantifiers-limit}
![](examples/regex/quantifier_limit.py)


## Quantifiers on character classes
{id: quantifiers-on-character-class}
![](examples/regex/quantifier_on_character_class.py)


## Greedy quantifiers
{id: greedy-quantifiers}
![](examples/regex/greedy.py)

{aside}

They match 'xaaa', 'xa' and '' respectively.
{/aside}


## Minimal quantifiers
{id: minimal-quantifiers}
![](examples/regex/minimal.py)


## Anchors
{id: anchors}
{i: \A}
{i: \Z}
{i: ^}
{i: $}

* \A matches the beginning of the string
* \Z matches the end of the string
* ^ matches the beginning of the row (see also re.MULTILINE)
* $ matches the end of the row but will accept a trailing newline (see also re.MULTILINE)

![](examples/regex/anchors.py)
![](examples/regex/anchors.out)

## Anchors with mulitline
{id: anchors-with-multiline}


![](examples/regex/anchors_multiline.py)


## Anchors on both end
{id: anchors-both-end}

![](examples/regex/anchors_both.py)
![](examples/regex/anchors_both.out)

## Match ISBN numbers
{id: matching-isbn}

```
```
![](examples/regex/isbn.py)


## Matching a section
{id: matching-section}
![](examples/regex/matching_section.py)


## Matching a section - minimal
{id: matching-section-minimal}
![](examples/regex/matching_section_minimal.py)


## Matching a section negated character class
{id: matching-section-with-negated-character-class}
![](examples/regex/negated_character_class.py)




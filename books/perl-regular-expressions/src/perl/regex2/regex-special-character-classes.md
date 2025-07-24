# Special character classes

* \w
* \d
* \s
* ^
* $

|  Expression  |  Meaning  | Usage |
|    \w        |  Word characters: [a-zA-Z0-9_] | \w+ or [\w#-]+ |
|    \d        |  Digits: [0-9]  |  |
|    \s        |  [\f\t\n\r ] form-feed, tab, newline, carriage return and SPACE |  |
|    \W        |  [^\w] |  |
|    \D        |  [^\d] |  |
|    \S        |  [^\s] |  |
|    [:class:] |  POSIX character classes (alpha, alnum...)  | [:alpha:]+  or  [[:alpha:]#-]+ |
|    \p{...}   |  Unicode definitions (IsAlpha, IsLower, IsHebrew, ...) | \p{IsHebrew}+   or [\p{IsHebrew}#!-] |
|    \P{...}   |  Negation of Unicode character class |  |


See also `perldoc perlre` and `perldoc perluniintro`.



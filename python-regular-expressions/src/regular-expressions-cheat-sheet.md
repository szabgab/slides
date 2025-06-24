# Regular Expressions Cheat sheet

|  Expression  |  Meaning  |
|    a         |  Just an 'a' character  |
|    .         |  any character except new-line  |
|    [bgh.]    |  one of the chars listed in the character class b,g,h or . |
|    [b-h]     |  The same as [bcdefgh]  |
|    [a-z]     |  Lower case letters  |
|    [b-]      |  The letter b or -  |
|    [^bx]     |  Anything except b or x  |
|    \w        |  Word characters: [a-zA-Z0-9_]  |
|    \d        |  Digits: [0-9]  |
|    \s        |  [\f\t\n\r ] form-feed, tab, newline, carriage return and SPACE |
|    \W        |  [^\w] |
|    \D        |  [^\d] |
|    \S        |  [^\s] |
|    a*        |  0-infinite  'a' characters  |
|    a+        |  1-infinite  'a' characters  |
|    a?        |  0-1         'a' characters  |
|    a{n,m}    |  n-m         'a' characters  |
|    ( )       |  Grouping and capturing  |
|    |         |  Alternation  |
|    \1, \2    |  Capture buffers  |
|    ^ $       |  Beginning and end of string anchors  |


[re](http://docs.python.org/library/re.html)






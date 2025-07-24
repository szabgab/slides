# Solutions: Regular expressions

* has a 'q' `/q/`
* starts with a 'q' `/^q/`
* has 'th' `/th/`
* has an 'q' or a 'Q' `/[qQ]/`
* has a `*` in it `/\*/`
* another solution: `/[*]/`
* starts with an 'q' or an 'Q' `/^[qQ]/`
* has both 'a' and 'e' in it `$str =~ /a/ and $str =~ /e/`
* has an 'a' and somewhere later an 'e' `/a.*e/`
* does not have an 'a' `$str !~ /a/`  Not good: `/[^a]/`
* does not have an 'a' nor 'e' `$str !~ /[ae]/`
* has an 'a' but not 'e' **$str =~ /a/ and $str !~ /e/**
* has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear" **/[aeiou]{2}/**
* has at least 3 vowels  **/[aeiou].*[aeiou].*[aeiou]/**
* has at least 6 characters **/....../**
* another solution: **/.{6}/**
* yet another solution: **length($str) >= 6**
* has at exactly 6 characters: **length($str) == 6**
* all the words with either 'Bar' or 'Baz' in them  **/Ba[rz]/**
* all the rows with either 'apple pie' or 'banana pie' in them `if ($row =~ /apple pie/ or $row =~ /banana pie/){ }`
* for each row print if it was apple or banana pie?


```
my $ok;
if ($row =~ /apple pie/) {
     print "apple\n";
     $ok = 1;
} elsif ($row =~ /banana pie/) {
     print "banana\n";
     $ok = 1;
}
```



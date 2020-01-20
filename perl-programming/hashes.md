# Hashes
{id: hashes}





## What is a hash?
{id: what-is-a-hash}
{i: %}
{i: hash}
{i: associative array}

* Unordered group of key/value pairs where
* key is a unique string
* value is any scalar


* Associative Arrays in PHP
* Dictionary in Python



## Uses of hashes
{id: uses-of-hashes}


Mapping of single feature of many similar items:



* phone book (name => phone number)
* worker list (ID number => name)
* CGI: (fieldname => field value)



Features of an object:



* Information about a person (fname, lname, email, phone, ...)



## Creating hashes
{id: creating-hashes}

```
my %user;
%user = ("fname", "Foo", "lname", "Bar");

my %user = (
    "fname", "Foo", 
    "lname", "Bar",
    );

my %user = (
    fname => "Foo",
    lname => "Bar",
    );

print $user{"fname"}, "\n";
print $user{fname}, "\n";

my $key = "fname";
print $user{$key}, "\n";


$user{fname} = 'Moo';
$user{email} = 'foo@bar.com';
```


## Create hash from an array
{id: create-hash-from-array}

```
my %user = qw(fname Foo lname Bar);

my @person = qw(fname Foo lname Bar);
my %user = @person;

my @foobar = %user;
print "@foobar\n"; # fname Foo lname Bar
                   # or
print "@foobar\n"; # lname Bar fname Foo 



$user{phone} = '123-456';     # change the value of one element
                              # or add key/value pair

%user = (phone => '123-456'); # change the hash
                              # remove all previous elements from the hash
                              # add a single key/value pair
```


## Hash in scalar context
{id: hash-in-scalar-context}


A hash in LIST context returns its keys and values.



```
my @foobar = %user;
```


In SCALAR context:



```
if (%user) {
    # the hash is not empty
}
```


## Fetching data from hash
{id: fetching-data-from-hash}
{i: keys}
{i: sort keys}

```
my @fields = keys %user;
foreach my $field (@fields) {
    print "$field    $user{$field}\n";
}


foreach my $field (keys %user) {
    print "$field    $user{$field}\n";
}


my @fields = keys %user;
my @sorted_fields = sort @fields;
foreach my $field (@sorted_fields) {
    print "$field    $user{$field}\n";
}

foreach my $field (sort keys %user) {
    print "$field    $user{$field}\n";
}
```


## exists, delete hash element
{id: hash-exists-delete}
{i: exists}
{i: delete}
{i: Data::Dumper}
![](examples/hashes/exists.pl)
![](examples/hashes/exists.out)


## Multi dimensional hashes
{id: multi-dimensional-hash}
{i: Data::Dumper}
![](examples/hashes/grades.pl)
![](examples/hashes/grades.out)



## Count words
{id: count-words}
![](examples/hashes/count_words_hash.pl)


## Exercise: Parse HTTP values
{id: exercise-parse-http-values}

```
You get one line like the following:
fname=Foo&amp;lname=Bar&amp;phone=123&amp;email=foo@bar.com

Build a hash table from it so:
print $h{fname};      #  Foo 
print $h{lname};      #  Bar
...

Start with this file:
```
![](examples/hashes/split_http_skeleton.pl)
![](examples/hashes/split_http.out)


## Exercise: Improve the color selector
{id: exercise-improve-color-selector}

```
In the external file where we defined the colors, for each color
keep also a character that will be used to display the menu:
```
![](examples/hashes/color_map.txt)

```
When displaying the menu show:

y) yellow
z) brown
b) black
e) blue

and wait till the user selects the appropriate letter.

Allow the user to provide a color on the command line
using the --color option and check if that is one of
the valid colors.

When reading in the file describing the menu options,
check for duplicate use of the same letter.
```


## Exercise: Display scores
{id: exercise-display-scores}

```
Read in a file where on each line there is a name and a score  
with a comma between them. 
Print them sorted based on name.
Then also print sorted based on score.
```
![](examples/hashes/score_data.txt)


## Exercise: Analyze Apache log file
{id: exercise-analyze-apache-hash}

```
In the files section earlier we had a an example counting
how many hits came from localhost and from other places.

Please improve that analyzer to provide a report:
which client IP address were used and how many hits were from
each IP address.

The log file can be found here:
examples/files/apache_access.log
```


## Exercise: Parse variable width fields
{id: exercise-parse-variable-width-fields}
![](examples/hashes/variable_width_fields.log)



## Solution: Parse HTTP values
{id: solution-parse-http-values}
![](examples/hashes/split_http.pl)


## Solution: Improve the color selector
{id: solution-improve-color-selector}
![](examples/hashes/color_selector_file.pl)


## Solution: Display scores
{id: solution-display-scores}
![](examples/hashes/score_data.pl)


## Solution: Analyze Apache log file
{id: solution-analyze-apache-hash}
![](examples/hashes/apache_log_hosts_hash.pl)


## Solution: Parse variable width fields
{id: solution-parse-variable-width-fields}
![](examples/hashes/parse_variable_width_fields.pl)




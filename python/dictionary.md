# Dictionary (hash)
{id: python-dictionary}

## What is a dictionary
{id: what-is-a-dictionary}

* Unordered key-value pairs.
* Keys are immutables (numbers, strings, tuples).
* Values can be any object.


## When to use dictionaries
{id: when-to-use-dictionaries}

* ID to Name mapping.
* Object to Count mapping.
* Name of a feature to value of the feature.
* Name of an attribute to value of the attribute.

## Various dictionary examples
{id: various-dictionary-examples}

![](examples/dictionary/person.py)

![](examples/dictionary/people.py)

![](examples/dictionary/people.out)


## Dictionary
{id: dictionary}
{i: dictionary}
{i: dict}
{i: {}}

* We can start from an empty dictionary and then fill it witg key-value pairs.

![](examples/dictionary/dict.py)

## Create dictionary
{id: create-dictionary-with-data}

* We can also start with a dictionary that already has some data in it.

![](examples/dictionary/create_dictionary.py)


## keys
{id: dictionary-keys}
{i: keys}

* Sometimes we don't know up front what keys we might have

![](examples/dictionary/planets.txt)

![](examples/dictionary/keys.py)

* Keys are returned in seemingly random order.


## Loop over keys
{id: loop-over-keys}
{i: keys}

![](examples/dictionary/loop_keys.py)

## Loop over dictionary keys
{id: loop-over-dictionary-keys}

Looping over the "dictionary" is just like looping over the keys, but personally I prefer when we use the `somedictionary.keys()` expression.

![](examples/dictionary/loop_dictionary.py)



## Loop using items
{id: loop-items}
{i: items}

![](examples/dictionary/loop_items_kv.py)
![](examples/dictionary/loop_items_kv.out)

![](examples/dictionary/loop_items.py)


## values
{id: dictionary-values}
{i: values}

* Values are returned in the same random order as the keys are.

![](examples/dictionary/values.py)


## Not existing key
{id: not-existing-key}

If we try to fetch the value of a key that does not exist, we get an exception.

![](examples/dictionary/no_such_key.py)
![](examples/dictionary/no_such_key.out)


## Get key
{id: get-key}
{i: get}

If we use the `get` method, we get `None` if the key does not exist.

![](examples/dictionary/get_key.py)
![](examples/dictionary/get_key.out)

`None` will be interpreted as `False`, if checked as a boolean.


## Does the key exist?
{id: key-exists}
{i: exists}
{i: in}

![](examples/dictionary/exists.py)
![](examples/dictionary/exists.out)


## Does the value exist?
{id: value-exists}
{i: values}

![](examples/dictionary/in_values.py)
![](examples/dictionary/in_values.out)


## Delete key
{id: delete-key}
{i: del}
{i: pop}

![](examples/dictionary/delete.py)
![](examples/dictionary/delete.out)


## List of dictionaries
{id: list-of-dicts}

![](examples/dictionary/list_of_dicts.py)
![](examples/dictionary/list_of_dicts.out)


## Shared dictionary
{id: shared-dictionary}

![](examples/dictionary/shared_memory.py)
![](examples/dictionary/shared_memory.out)


## immutable collection: tuple as dictionary key
{id: tuple-as-key}

![](examples/dictionary/tuple_as_key.py)
![](examples/dictionary/tuple_as_key.out)


## immutable numbers: numbers as dictionary key
{id: numbers-as-key}

![](examples/dictionary/numbers.py)
![](examples/dictionary/numbers.out)


## Sort a dictionary
{id: sort-dictionary}

{aside}
When people says "sort a dictionary" they usually mean sorting the keys of the dictionary, but what does it mean in Python if we call `sorted` on a dictionary?
{/aside}

![](examples/dictionary/sort_dictionary.py)

## Sort dictionary values
{id: sort-dictionary-values}

![](examples/dictionary/sort_dictionary_values.py)

## Sort dictionary by value
{id: sort-dictionary-by-value}

* Sort the keys by the values

![](examples/dictionary/sort_dictionary_by_values.py)

![](examples/dictionary/sort_dictionary_by_values_getitem.py)


## Sort dictionary keys by value (another example)
{id: sort-keys-by-value}
{i: sort}
{i: key}

![](examples/dictionary/scores.py)
![](examples/dictionary/scores.out)

## Insertion Order is kept
{id: insertion-order}

Since Python 3.7

![](examples/dictionary/insertion_order.py)
![](examples/dictionary/insertion_order.out)

## Change order of keys in dictionary - OrderedDict
{id: change-order-of-keys}
{i: collections}
{i: OrderedDict}

![](examples/dictionary/change_order.py)
![](examples/dictionary/change_order.out)


## Set order of keys in dictionary - OrderedDict
{id: set-order-of-keys}
{i: collections}
{i: OrderedDict}

![](examples/dictionary/set_order.py)
![](examples/dictionary/set_order.out)

## Setdefault
{id: setdefault}

{aside}
Trying to access a key in a dictionary that does not exist will result a KeyError exception.

Using the `get` method we can avoid this. The `get` method, will return the value of the key if the key exists. None if the key does not exists, or a default value if it was supplied to the `get` method.
This will not change the dictionary.

Using the `setdefault` method is similar to the `get` method but it will also create the key with the given value.
{/aside}


![](examples/dictionary/setdefault.py)


## Exercise: count characters
{id: exercise-count-characters}

* Write a script called **count_characters.py** that given a long text will count how many times each character appears.
* Change the code so it will be able to count characters in a file.

![](examples/dictionary/count_characters_skeleton.py)


## Exercise: count words
{id: exercise-count-words}

* Create script called **count_words.py**
* Skeleton:

![](examples/dictionary/count_words_skeleton.py)

Expected output: (the order is not important)

```
Wombat:1
Rhino:2
Sloth:3
Tarantula:1
```


## Exercise: count words from a file
{id: exercise-count-words-in-file}


Create a script called **count_words_from_a_file.py** that given a file with words and spaces and newlines only, count how many times each word appears.


![](examples/dictionary/words_and_spaces.txt)

* Based on [Lorem Ipsum](https://www.lipsum.com/)


Expected result for the above file:

![](examples/dictionary/words_and_spaces_counted.txt)


## Exercise: Apache log
{id: exercise-apache-log}


Every web server logs the visitors and their requests in a log file. The Apache web server has a log file similar
to the following file. (Though I have trimmed the lines for the exercise.) Each line is a "hit", a request from
the browser of a visitor.

Each line starts with the IP address of the visitor. e.g. 217.0.22.3.

Create a script called **apache_log_parser.py** that given sucha a log file from Apache, report how many hits (line were from each IP address.

![](examples/dictionary/apache_access.log)

Expected output:


```
127.0.0.1         12
139.12.0.2         2
217.0.22.3         7
```


## Exercise: Combine lists again
{id: exercise-combine-lists-again}

See the same exercise in the previous chapter. Use the filename **combine_lists_using_dictionary.py**.


## Exercise: counting DNA bases
{id: exercise-counting-dna-bases}

Write a script called **count_dna_bases.py** that given a sequence like this: "ACTNGTGCTYGATRGTAGCYXGTN",
will print out the distribution of the elemnts to get the following result:

```
A 3 - 12.50 %
C 3 - 12.50 %
G 6 - 25.00 %
N 2 -  8.33 %
R 1 -  4.17 %
T 6 - 25.00 %
X 1 -  4.17 %
Y 2 -  8.33 %
```


## Exercise: Count Amino Acids
{id: exercise-count-amino-acids}

* Each sequence consists of many repetition of the 4 bases represented by the ACTG characters.
* There are 64 codons (sets of 3 bases following each other)
* There are 20 [Amino Acids](https://en.wikipedia.org/wiki/Amino_acid) each of them are represented by 3 bases (by one codon).
* Some of the Amino Acids can be represented in multiple ways, represented in the [Codon Table](https://en.wikipedia.org/wiki/DNA_codon_table). For example Histidine can be encoded by both CAU, CAC

* Create a file called **count_amino_acids.py** that given a file witha  DNA sequence in it, will count the Amino acids from the sequence.
* Read the sequence saved in a txt file.
* You can generate a sequence with a random number generator and save it to that file, but it would be much better if you used a real sequence.
* An even better way would be to read the sequence from a FASTA file. You can download one from [NCBI](https://www.ncbi.nlm.nih.gov/).

* Skeleton:

![](examples/dictionary/count_amino_acids_skeleton.py)

* You will want to convert this to a dictionary that maps each codon to an Amino Acid. Do it programmatically!


## Exercise: List of dictionaries
{id: exercise-list-of-dictionaries}

Given the following file build a list of dictionaries where each dictionary represents one person.
The keys in the dictionary are the names of the columns (fname, lname, born) the values are the respective values from each row.
Create a file called **list_of_dictionaries.py**.

![](examples/csv/monty_python.csv)

* Skeleton

![](examples/dictionary/list_of_dictionaries_skeleton.py)

## Exercise: Dictionary of dictionaries
{id: exercise-dictionary-of-dictionaries}

Given the following file build a dictionary of dictionaries where each internal dictionary represents one person.
The keys in the internal dictionaries are the names of the columns (fname, lname, born) the values are the respective values from each row.
In the outer dictionary the keys are the (fname, lname) tuples.
Create a file called **dictionary_of_dictionaries.py**

![](examples/csv/monty_python.csv)

Skeleton:

![](examples/dictionary/dictionary_of_dictionaries_skeleton.py)

## Exercise: Age limit with dictionaries
{id: exercise-age-limit-with-dictionaries}

* Create a file called **age_limit_with_dictionary.py**
* Ask the user what is their age and in which country are they located.
* Tell them if they can legally drink alcohol.
* See the [Legal drinking age](https://en.wikipedia.org/wiki/Legal_drinking_age) list.

* Given a file like the following create a new file with a third column in which you write "yes", or "no" depending if the person can legally drink alcohol in that country.

## Exercise: Merge files with timestamps
{id: exercise-merge-files-with-timestamps}

* Write a script called **merge_files_with_timestamps.py**
* Given a few CSV files in which the first column is a timestamp, write a script that can merge the files so the merged result also has timestamps in increasing order.
* First try to solve it for 2 files.
* Then solve it for any N files.

![](examples/dictionary/merge/a.csv)
![](examples/dictionary/merge/b.csv)
![](examples/dictionary/merge/c.csv)
![](examples/dictionary/merge/d.csv)


## Solution: count characters
{id: solution-count-characters}

![](examples/dictionary/count_characters.py)

* We need to store the counter somewhere. We could use two lists for that, but that would give a complex solution that runs in O(n**2) time.
* Besides, we are in the chapter about dictionaries so probably we better use a dictionary.
* In the `count` dictionary we each key is going to be one of the characters and the respective value will be the number of times it appeared.
* So if out string is "aabx" then we'll end up with

```
{
    "a": 2,
    "b": 1,
    "x": 1,
}
```

* The `for in` loop on a string will iterate over it character by charter (even if we don't call our variable `char`.
* We check if the current character is a newline `\n` and if it we call `continue` to skip the rest of the iteration. We don't want to count newlines.
* Then we check if we have already seen this character. That is, it is already one of the keys in the `count` dictionary. If not yet, then we add it and put 1 as the values. After all we saw one copy of this character. If we have already seen this character (we get to the `else` part) then we increment the counter for this character.
* We are done now with the data collection.

* In the second loop we go over the keys of the dictionary, that is the characters we have encountered. We sort them in ASCII order.
* Then we print each one of them and the respective value, the number of times the character was found.

## Default Dict
{id: default-dict}
{i: collections}
{i: defaultdict}

![](examples/dictionary/counter.py)
![](examples/dictionary/counter.out)

![](examples/dictionary/counter_condition.py)
![](examples/dictionary/counter_condition.out)

![](examples/dictionary/default_dict.py)
![](examples/dictionary/default_dict.out)

## Solution: count characters with default dict
{id: solution-count-characters-with-default-dict}
{i: collections}
{i: defaultdict}


![](examples/dictionary/count_characters_default_dict.py)

* The previous solution can be slightly improved by using `defaultdict` from the `collections` module.
* `count = defaultdict(int)` creates an empty dictionary that has the special feature that if you try to use a key that does not exists, it pretends that it exists and that it has a value 0.
* This allows us to remove the condition checking if the character was already seen and just increment the counter. The first time we encounter a charcter the dictionary will pretend that it was already there with value 0 so everying will work out nicely.


## Solution: count words (plain)
{id: solution-count-words}

![](examples/dictionary/count_words.py)

## Solution: count words (defaultdict)
{id: solution-count-words-defaultdict}
{i: defaultdict}

* [defaultdict](https://docs.python.org/library/collections.html#collections.defaultdict)

![](examples/dictionary/count_words_with_defaultdict.py)

## Solution: count words (Counter)
{id: solution-count-words-counter}
{i: Counter}

* [Counter](https://docs.python.org/library/collections.html#collections.Counter)

![](examples/dictionary/count_words_with_counter.py)


## Solution: count words in file
{id: solution-count-words-in-file}

![](examples/dictionary/count_words_in_file.py)


## Solution: Apache log
{id: solution-apache-log}

![](examples/dictionary/apache_access.py)

## Solution: Apache log using split
{id: solution-apache-log-using-split}

![](examples/dictionary/apache_access_split.py)


## Solution: Combine files
{id: solution-combine-files}

* This is a working, but very verbose solution. Check out the next one!

![](examples/dictionary/combine_files.py)

## Solution: Combine files-improved
{id: solution-combine-files-improved}

![](examples/dictionary/combine_files_improved.py)


## Solution: counting DNA bases
{id: solution-counting-dna-bases}

![](examples/dictionary/counting_dna_bases.py)


## Solution: Count Amino Acids
{id: solution-count-amino-acids}

Generate random DNA sequence

![](examples/dictionary/generate_dna.py)

![](examples/dictionary/count_amino_acids.py)

![](examples/dictionary/amino_acid_counter.py)

## Solution: List of dictionaries
{id: solution-list-of-dictionaries}

![](examples/dictionary/list_of_dictionaries.py)

* [csv](https://docs.python.org/library/csv.html)

![](examples/dictionary/list_of_dictionaries_csv.py)

## Solution: Dictionary of dictionaries
{id: solution-dictionary-of-dictionaries}

![](examples/dictionary/dictionary_of_dictionaries.py)

![](examples/dictionary/dictionary_of_dictionaries_csv.py)

## Solution: Age limit with dictionaries
{id: solution-age-limit-with-dictionaries}

![](examples/dictionary/legal_drinking.py)

## Solution: Merge files with timestamps
{id: solution-merge-files-with-timestamps}

![](examples/dictionary/merge/merge.py)
![](examples/dictionary/merge/merge_all.py)

## Do not change dictionary in loop
{id: do-not-change-in-loop}

![](examples/dictionary/change_in_loop.py)

## Named tuple (sort of immutable dictionary)
{id: namedtuple}
{i: namedtuple}

* A bit like an immutable dictionary

![](examples/dictionary/namedtuple.py)

## Create dictionary from List
{id: create-dictionary-from-list}

![](examples/dictionary/dict_from_list.py)
![](examples/dictionary/dict_from_list.out)


## Sort Hungarian letters (lookup table)
{id: sort-hungarian-letters}

![](examples/dictionary/sort_hungarian_letters.py)



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



## Dictionary
{id: dictionary}
{i: dictionary}
{i: dict}
{i: {}}
![](examples/dictionary/dict.py)


## keys
{id: dictionary-keys}
{i: keys}
![](examples/dictionary/keys.py)

* Keys are returned in seemingly random order.



## Loop over keys
{id: loop-over-keys}
{i: keys}
![](examples/dictionary/loop_keys.py)


## Loop using items
{id: loop-items}
{i: items}
![](examples/dictionary/loop_items.py)
![](examples/dictionary/loop_items_kv.py)


## values
{id: dictionary-values}
{i: values}

* Values are returned in the same random order as the keys are.

![](examples/dictionary/values.py)



## Not existing key
{id: not-existing-key}

If we try to fetch the value of a key that does not exist, we get an exception.

![](examples/dictionary/no_such_key.py)


## Get key
{id: get-key}
{i: get}

If we use the **get** method, we get **None** if the key does not exist.

![](examples/dictionary/get_key.py)

None will be interpreted as False, if checked as a boolean.



## Does the key exist?
{id: key-exists}
{i: exists}
{i: in}
![](examples/dictionary/exists.py)


## Does the value exist?
{id: value-exists}
{i: values}
![](examples/dictionary/in_values.py)



## Delete key
{id: delete-key}
{i: del}
{i: pop}
![](examples/dictionary/delete.py)


## List of dictionaries
{id: list-of-dicts}
![](examples/dictionary/list_of_dicts.py)

```
[{'name': 'Foo Bar', 'email': 'foo@example.com'}, {'name': 'Qux Bar', 'email': 'qux@example.com',
'address': 'Borg, Country', 'children': ['Alpha', 'Beta']}]

Foo Bar
Alpha

['Foo Bar', 'Qux Bar']
```


## Shared dictionary
{id: shared-dictionary}

![](examples/dictionary/shared_memory.py)


## immutable collection: tuple as dictionary key
{id: tuple-as-key}

![](examples/dictionary/tuple_as_key.py)
![](examples/dictionary/tuple_as_key.out)


## immutable numbers: numbers as dictionary key
{id: numbers-as-key}

![](examples/dictionary/numbers.py)
![](examples/dictionary/numbers.out)


## Sort dictionary keys by value
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



## Exercise: count characters
{id: exercise-count-characters}

Given a long text, count how many times each character appears?

![](examples/dictionary/count_characters_skeleton.py)

Extra credit: Change the code so it will be able to count characters of a file.



## Exercise: count words
{id: exercise-count-words}



Part of the code:



```
words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']
```



Expected output: (the order is not important)




```
Wombat:1
Rhino:2
Sloth:3
Tarantula:1
```



## Exercise: count words from a file
{id: exercise-count-words-in-file}


Given a file with words and spaces and newlines only, count how many times each word appears.


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

Given sucha a log file from Apache, report how many hits (line were from each IP address.


![](examples/dictionary/apache_access.log)

Expected output:


```
127.0.0.1         12
139.12.0.2         2
217.0.22.3         7
```


## Exercise: Combine lists again
{id: exercise-combine-lists-again}

See the same exercise in the previous chapter.



## Exercise: counting DNA bases
{id: exercise-counting-dna-bases}


Given a sequence like this: "ACTNGTGCTYGATRGTAGCYXGTN",
print out the distribution of the elemnts to get the following result:



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
* There are 22 [Amino Acids](https://en.wikipedia.org/wiki/Amino_acid) each of them are represented by 3 bases.
* Some of the Amino Acids can be represented in multiple ways. For example Histidine can be encoded by both CAU, CAC)
* We have a DNA sequence
* Count the Amino acids form the sequence. (For our purposes feel free to generate a DNA sequence with a random number generator.



## Solution: count characters
{id: solution-count-characters}
![](examples/dictionary/count_characters.py)


## Solution: count words
{id: solution-count-words}
![](examples/dictionary/count_words.py)
![](examples/dictionary/count_words_with_counter.py)
![](examples/dictionary/count_words_with_defaultdict.py)


## Solution: count words in file
{id: solution-count-words-in-file}
![](examples/dictionary/count_words_in_file.py)


## Solution: Apache log
{id: solution-apache-log}
![](examples/dictionary/apache_access.py)


## Solution: Combine lists again
{id: solution-combine-lists-again}
![](examples/dictionary/combine_lists.py)


## Solution: counting DNA bases
{id: solution-counting-dna-bases}
![](examples/dictionary/counting_dna_bases.py)


## Solution: Count Amino Acids
{id: solution-count-amino-acids}

Generate random DNA sequence

![](examples/dictionary/generate_dna.py)

![](examples/dictionary/count_amino_acids.py)


## Loop over dictionary keys
{id: loop-over-dictionary-keys}

Looping over the "dictionary" is just like looping over the keys.

![](examples/dictionary/loop_dictionary.py)


## Do not change dictionary in loop
{id: do-not-change-in-loop}
![](examples/dictionary/change_in_loop.py)




# Exercise: collect packets

* You get a series of packets (e.g. lines in a file)
* In each line you have several fields: id, seqid, maxseq, content
* id is a unique identifier of a series of packets (lines)
* seqid is the seuence id of a packet in a series. (an integer)
* maxseq is the length of the sequence.
* content is the actual content.

In each iteration return a message that is built up from all the packages in the given sequence.

{% embed include file="src/examples/iterators/packets/packets.txt" %}

**Output:**

{% embed include file="src/examples/iterators/packets/packets.out" %}

{% embed include file="src/examples/iterators/packets/packets1.txt" %}

{% embed include file="src/examples/iterators/packets/packets2.txt" %}



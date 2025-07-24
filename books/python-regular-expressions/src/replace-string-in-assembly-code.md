# Replace string in Assembly code

At a company we had some Assembly code that looks like the text file. In case you don't know, [Assembly](https://en.wikipedia.org/wiki/Assembly_language) is
a very low level programming language. Here we have some sample code that uses variables like A and registers like R1, R2, and R3.

We had this code, but because the hardware changed we had to make changes to the code and rename the registies R1 to be R2, R2 to be R3, and R3 to be R1.
We cannot just simple do these steps one after the other becasue once we renamed R1 to be R2 we won't know which of the R2-s do we need to rename and which
are new. So someone came up with the idea to use R4 as a temporary name and start by renaming R1 to R4,  R3 to R1, R2 to R3, and finally the temporary R4 to R2.

As you could see in our solution coed.

It worked all very smoothly till we turned on the device that immediately emitted smoke. It did not pass the "smoke test".

As it turns out in the original text there were also R4 registers that we have not noticed and they were all renamed to be R2.

The first idea to improve our converter program was to use some other temporary string that for sure cannot be in the code, such as QQRQ, but then
we arrived to the conclusion that there are better ways to solve this.

{% embed include file="src/examples/regex/assembly_source.txt" %}

{% embed include file="src/examples/regex/assembly_process.py" %}



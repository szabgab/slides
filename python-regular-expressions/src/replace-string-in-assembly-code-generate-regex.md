# Replace string in Assembly code - generate regex

In this solution we generate the regex from the keys of the mapping dictionary.

Once we have this we also opened other opportunities for improvement. Now that all the replacement mapping
comes from a regex we have separated the "data" from the "code". We can now decide to read in the mapping
from an Excel file (for example). That way we can hand over the mapping creation to someone who does not know
Python. Our code will take that file, read the mapping from the spreadsheet, create the mapping dictionary,
create the regex and do the work.

{% embed include file="src/examples/regex/assembly_process_generate.py" %}




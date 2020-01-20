# One-liners
{id: oneliners}

## One-liner: print
{id: perl-one-liner-print}
{i: -e|command line}
{i: -E}

**perl -e "print 42"**


**perl -E "say 42"**


**perl -E "say q(hello world)"**



## One-liner: Rename many files
{id: perl-one-liner-rename-files}
{i: rename}
{i: glob}

**perl -e "rename $_, $_ . '.old' for glob '*.log'"**


**perl -e "$t = time; rename $_, substr($_, 0, -3) . $t for glob '*.log'"**



## One-liner: grep on Windows as well
{id: perl-one-liner-grep-on-window-as-well}

Lacking grep on Windows, search for all the occurrences 
of the 'secret' in my xml files.



In a single file:


**perl -ne "print $_ if /secret/" main.xml**


As Windows does not know how to handle wildcards on the command line,
we cannot supply *.xml and expect it to handle all the xml files.
We help it with a small BEGIN block. $ARGV holds the name of the current file
</p> 

**perl -ne "BEGIN{ @ARGV = glob '*.xml'} print qq{$ARGV:$_} if /secret/"**



## One-liner: Replace a string in many files
{id: perl-one-liner-replace-file-content}
<indexterm><primary>-i</primary></indexterm>
<indexterm><primary>-p</primary></indexterm>
<literallayout> 
You have a bunch of text files in your directory mentioning the name:
   
"Microsoft Word"

You are told to replace that by 
    
"OpenOffice Write"
</literallayout> 

**perl -i -p -e "s/Microsoft Word/OpenOffice Write/g" *.txt**

<literallayout> 
-i = inplace editing
-p = loop over lines and print each line (after processing)
-e = command line script
</literallayout> 


## One-liner: Change encoding
{id: perl-oneliner-change-encoding}
<indexterm><primary>-i</primary></indexterm>
<indexterm><primary>-M</primary></indexterm>
<indexterm><primary>-p</primary></indexterm>
<indexterm><primary>Encode</primary></indexterm>


Convert all the .srt files that are Windows Hebrew encoded to UTF-8 keeping a backup copy
of the original file with a .bak extension.



```
-i    - inplace editing
.bak  - generate backup with that extension
-M    - load  module as 'use' would do
-p    - go over line by line on the file, put the line in $_, execute the
        command on it and then print the result.
        In case of inplace editing, save it back to the file.
```

**perl -i.bak -MEncode -p -e "Encode::from_to($_, 'Windows-1255', 'utf-8')" video.srt**

![](examples/oneliners/encode_files.pl)


## One-liner: print the 3rd field of every line in a CSV file
{id: oneliner-process-csv-file}
{i: CSV}
{i: -n}
{i: -a}
{i: -F}

```
You have a number of csv files, 
you want to print the 3rd field of each row of each file.
```

**perl -n -a -F, -e 'print "$F[2]\n"' *.csv**


```
-n  = loop over lines but do NOT print them 
-a  = autosplit by ' '
-F, = replace the split string by ','
```


You want to make sure all the rows are 4 elements long.
Print out file name and line number of all the bad rows.



**perl -a -F, -n -e 'print "$ARGV:$.\n" if @F != 4' data.csv**



## One-liner: Print all usernames from /etc/passwd
{id: perl-one-liner-print-usernames}

**perl -n -a -F: -e 'print "$F[0]\n"' /etc/passwd**






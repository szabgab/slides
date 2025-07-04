# Generating HTML reports from Archives



Once you have the tar.gz file on the central machine you should
be able to create the HTML report.
Unfortunately I could not find a nice way to do it but with the help
of Ash Berlin and Steve Purkis we came up with workaround:

First unzip the file using

    tar xzf tap.tar.gz

Then you can run the following command:

    prove --exec 'cat' -Q --formatter=TAP::Formatter::HTML t/ > output.html

This will only work on Unix, maybe on Windows one can replace 'cat' with
'type' but I have not tried it. In any case I hope soon there will a better
solution to this.



First unzip the file using `tar xzf tap.tar.gz`

Then you can run the following command

```
prove --exec 'cat' -Q --formatter=TAP::Formatter::HTML t/ > output.html
```





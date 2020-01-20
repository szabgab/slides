# Applications
{id: applications}





## Simple uses of Perl
{id: simple-uses-of-perl}


After leaning the syntax of the language let's see a few simple ways to use it in real life tasks.




## Create Unix user account
{id: create-unix-user}
![](examples/applications/create_user.pl)


## Reporting file system diskspace usage (df)
{id: available-diskspace}
{i: df}
![](examples/applications/diskspace.pl)

```
$ perl diskspace.pl ; df /
Total Size:             48062440 K
Available:              38720692 K
Used:                   9341748 K
Percent Full:           20 %
Total available to me:  36279216 K

Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/sda1             48062440   9341748  36279216  21% /
```


## Reporting diskspace usage on the mail server
{id: mailserver-diskspace-usage}
{i: du}
![](examples/applications/diskusage.pl)


## A du like script
{id: disk-usage}
{i: du}
![](examples/applications/du.pl)


## Send files by e-mail
{id: send-files}
{i: MIME}
![](examples/applications/send_files.pl)



## Read Excel file
{id: read-excel-file}
{i: Excel}
![](examples/applications/read_excel.pl)


<a href="https://perlmaven.com/create-an-excel-file-with-perl">How to create an Excel file with Perl.</a>





## Process file with fixed width records
{id: fixed-width-record}
![](examples/applications/pack.pl)
![](examples/applications/pack.txt)


## Process file with multiline records
{id: multiline-records}
![](examples/applications/config.txt)
![](examples/applications/process_config.pl)


<a href="https://perlmaven.com/how-to-read-a-csv-file-using-perl">How to read a CSV file using Perl?</a>






## Process multi field csv file
{id: process-multi-field-csv-file}
{i: csv}
![](examples/applications/fields.csv)
![](examples/applications/process_fields.pl)



## Fetch web page
{id: fetch-web-pages}
{i: http}
{i: web}
{i: GET}
{i: LWP::Simple}
![](examples/applications/get_webpage.pl)


## Generate web page
{id: generate-web-pages}
{i: CGI}
{i: HTML::Template}


We are building the HTML pages from a template utilizing the HTML::Template
module from CPAN. Besides the plain HTML the template has additional 
TMPL_* tags that will be filled by the values by HTML::Template.


![](examples/applications/html.tmpl)


This is a simple Perl script that should be installed to a CGIExec enabled directory 
of Apache. When the user hits this page the first time it displays a white page with only
entry-box and a submit button on it. the user can fill the box,  


![](examples/applications/html.pl)


## Parse XML file
{id: parse-xml}
{i: XML}
{i: XML::Simple}
![](examples/applications/simple.xml)
![](examples/applications/xml_simple.pl)


## Database access using DBI and DBD::SQLite
{id: database-using-dbi}
{i: database}
{i: DBI}
{i: DBD}
{i: SQLite}
![](examples/applications/db_create.pl)
![](examples/applications/db.pl)


<a href="https://perlmaven.com/simple-database-access-using-perl-dbi-and-sql">Simple Database access using Perl DBI and SQL</a>




## Net::LDAP
{id: net-ldap}
{i: LDAP}
{i: Net::LDAP}
![](examples/applications/ldap.pl)


<a href="https://perlmaven.com/reading-from-ldap-in-perl-using-net-ldap">Reading from LDAP in Perl using Net::LDAP</a>




## Tie::File
{id: tie-file}
{i: Tie::File}
![](examples/applications/tie.pl)






# MetaCPAN API

New API


* [MetaCPAN](https://metacpan.org/)
* [Moose](https://api-v1.metacpan.org/release/ETHER/Moose-2.1603)
* [100 most recent](https://api-v1.metacpan.org/release/_search?q=status:latest&amp;fields=name,status,date&amp;sort=date:desc&amp;size=100)
* api-v1 instead of api  and remove the v0/ from the path

Old API


* [100 most recent uploads](http://api.metacpan.org/v0/release/_search?q=status:latest&amp;fields=name,status,date&amp;sort=date:desc&amp;size=100)
* [Authors (limit 3)](http://api.metacpan.org/v0/author/_search?size=3)
* [Authors (show only 2 fields)](http://api.metacpan.org/v0/author/_search?size=3&amp;fields=pauseid,region)
* [Authors (show only PAUSEIDs with sz in them)](http://api.metacpan.org/v0/author/_search?size=3&amp;fields=pauseid,region&amp;q=sz)
* [Distributions](http://api.metacpan.org/v0/distribution/_search?size=3)
* [Distributions (name staring with DBIx)](http://api.metacpan.org/v0/distribution/_search?size=3&amp;q=DBIx)
* [Releases](http://api.metacpan.org/v0/release/_search?size=3)
* [Releases (show only specific fields and only for 'latest' releases](http://api.metacpan.org/v0/release/_search?size=3&amp;fields=author,distribution,status&amp;q=status:latest)
* [Releases (latest, authored by DAVID](http://api.metacpan.org/v0/release/_search?size=3&amp;fields=author,distribution,status&amp;q=status:latest%20AND%20author:DAVID)
* [Modules](http://api.metacpan.org/v0/module/_search?size=3)
* [Modules (called CGI)](http://api.metacpan.org/v0/module/_search?size=3&amp;q=name:CGI)
* [Modules (called CGI* , status:latest, list name and distribution)](http://api.metacpan.org/v0/module/_search?size=3&amp;q=name:CGI*%20AND%20status:latest&amp;fields=name,distribution)





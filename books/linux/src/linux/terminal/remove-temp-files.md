# Remove temp files

```
ls -l /tmp/ | grep "Jul  3" | cut -d ' ' -f 22 | xargs -I{} ls -ld /tmp/{} | less
ls -l /tmp/ | grep "Jul  3" | cut -d ' ' -f 22 | xargs -I{} rm -rf /tmp/{}

```

* List all the things in the /tmp directory
* Filter those that were created on "Jul  3".
* Limit the output to the filenames only.
* Execute rm -rf on all of them.



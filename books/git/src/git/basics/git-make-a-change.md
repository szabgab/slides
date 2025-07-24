# Making some changes

* diff
* --cached|diff

* edit the README.txt file again, adding a new row.
* $ git status
* $ git diff
* $ git add README.txt
* $ git status
* $ git diff
* $ git$ git diff --cached    (or --staged)


```
$ git status
```
{% embed include file="src/examples/out/status_03.txt" %}


What has changed?



```
$ git diff
```

```
WARNING: terminal is not fully functional
diff --git a/README.txt b/README.txt
index e51ca0d..a697828 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1,2 @@
-Hello Git
+Hello Git
+Second line
```


```
$ git add README.txt
$ git status
```
{% embed include file="src/examples/out/status_05.txt" %}


What did we change?


```
$ git diff
$ git diff --cached    (or --staged)
```


```
WARNING: terminal is not fully functional
diff --git a/README.txt b/README.txt
index e51ca0d..62567d0 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1,2 @@
-Hello Git
\ No newline at end of file
+Hello Git
+Second line
```


```
$ git commit -m "update README"
```

```
[master 1251a45] update README
 1 file changed, 2 insertions(+), 1 deletion(-)
```



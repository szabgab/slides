# So what was changed?


* git diff
* git diff --cached
* git diff HEAD

```
$ git diff

diff --git a/README.txt b/README.txt
index 62567d0..fb89137 100644
--- a/README.txt
+++ b/README.txt
@@ -1,2 +1,4 @@
 Hello Git
 Second line
+Third line
```

**Only the changes to the not staged files are shown**

```
$ git diff --cached
diff --git a/config.pl b/config.pl
index f9d55cd..e2b7f47 100644
--- a/config.pl
+++ b/config.pl
@@ -1 +1,2 @@
  this is the config.pl file
+ second line
```

**Only the changed to the staged files are shown**

```
$ git diff HEAD
diff --git a/README.txt b/README.txt
index 62567d0..fb89137 100644
--- a/README.txt
+++ b/README.txt
@@ -1,2 +1,4 @@
 Hello Git
 Second line
+Third line
+
diff --git a/config.pl b/config.pl
index f9d55cd..e2b7f47 100644
--- a/config.pl
+++ b/config.pl
@@ -1 +1,2 @@
  this is the config.pl file
+ second line
```

**changes between working copy and HEAD**




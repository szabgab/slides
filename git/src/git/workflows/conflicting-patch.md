# Conflicting patch

```
$ git am --show-current-patch

commit 6297d04c97c29937bcf540cf22312ec3900ae33e (master)
Author: A &lt;a@code-maven.com&gt;
Date:   Wed Jun 27 15:53:23 2018 +0300

    A at the bottom

diff --git a/README b/README
index 31d0540..a8a7095 100644
--- a/README
+++ b/README
@@ -2,3 +2,4 @@ Add line by a
 Another line by A
 Readme file
 2nd line
+line added by A
```



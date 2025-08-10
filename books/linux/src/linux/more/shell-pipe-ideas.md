# Shell Pipe ideas

```
sudo find /tmp/* -type d -cmin +30 -print0 | xargs -0 -I{} sudo ls -dl {} | wc -l
sudo find /tmp/* -type d -cmin +30 -print0 | xargs -0 -I{} sudo rm -rf {}

# The first commit of the README file:
git log README | grep ^commit | tail -1 | cut -d ' ' -f 2

Make a 1% sample of a large : separated accounting file
awk -F: 'rand() &lt; 0.01' accounting &gt; 1percent
```



# incoming, outgoing


git incoming - After a fetch it will show what is on the remote master barnch that I have not merged into my own master.


```
$ git log origin/master ^master
```


git outgoing - What is on my master that has not been pushed to the remote master


```
$ git log master ^origin/master
```



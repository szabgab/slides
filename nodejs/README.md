<sect1 id="complaints">
<title>Complaints</title>
<ul>
  <li>Indent forever? - No, you can name your functions.</li>
  <li></li>
</ul>
<text>
When doing tasks that really need to be done one after the other we need to:
   schedule something and give it a callback
       that will schedule a callback
          that will schedule a callback
             ....

The callbacks can be named functions and then you don't need to indent so deeply.
</text>
</sect1>

<!--
The other issues is that if we have several callback calling each other in our module
and we would like to allow someone to call the top-most sub but provide a callback to the
last one in the chain we could wrap the whole thing in a function that gets a callback and
passes that callback to its own callback and  so on till the last one that will actually
invoke that callback directly.

This is just an implementation detail inside a module that exposes a single function.


Another problem is that we lose stack-trace as each callback is called by the event-loop and
not the function that deployed it.
http://nodejs.org/illuminati0.pdf

-->



use let instead of var

Recursive listing of directory
Reading file line-by-line
tail on a file
run external process and print stdout and stderr


Chaining pipes
(e.g. use zlib.createGzip()  or zlib.createGunzip

tmeplate literals:
* Using backtick!
* In ES2015/ES6


Testing: https://medium.com/@me_37286/yoni-goldberg-javascript-nodejs-testing-best-practices-2b98924c9347


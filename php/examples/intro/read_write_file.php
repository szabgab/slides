

<h1>Read/Write files</h1>

<ul>
 <li> $fh = fopen("file", r);
 <ul>
   <li> other flags such as "w", "r+", "w+", "a", "a+", "x" (create if not exists), "x+" (... also read)
 </ul>
 <li> fclose($fh)
 <li> fwrite($fh, "something");
 <ul>
   <li> PHP closes the file at the end of the program but it is better practice to close it by ourself
 </ul>
 <li> $line = fgets($fh);
 <ul>
   <li> Reads a line
   <li> Need another variable to max the line length in old versions of PHP
 </ul>
 <li> $elements = fgetcsv($fh); 
 <ul>
   <li> returns an array of the values 
 </ul>
</ul>



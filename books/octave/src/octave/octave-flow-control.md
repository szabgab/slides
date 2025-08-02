# Flow Control

```
exit;    % exit the program
quit;    % exit the program


x = rand()
if x < 0.1,
    disp("very small");
elseif x < 0.5,
    disp("small");
else,
    disp("big");
end;


for i=1:10,
   v(i) = 2^i;
end;
v

indecies=1:10
for i=indecies,
   disp(i);
end;

i = 1;
while i <= 5,
   v(i) = 100
   i = i+1;
end;

while true,
   v(i) = 999;
   i = i+1
   if i == 6,
      break;
   end;
end;


% break and continue also work
```


Functions are the defined in their own .m files

```
function y = squareThisNumber(x)
y = x^2;
```

Then, if we are in the same directory as the .m file we can just type in:

```
squareThisNumber(5)
```

Octave search path:

```
addpath("/path/to/dir")
``` 

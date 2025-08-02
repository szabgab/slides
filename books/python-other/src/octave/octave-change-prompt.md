# Octave change interactive prompt

```
PS1('>>')
```

* Variables

```
a = 2
a = 2;  % supress echo of result
a = "text"
b = 'text'

pi      % 3.1416

disp(sprintf("%f is %0.2f",  pi, pi))   %  3.141593 is 3.14     C-like placeholders

```

* Matrix

```
>> A = [11 2; 3 4; 5 6]
A =

   11    2
    3    4
    5    6
```

* Matrix + scalar

```
>> A + 1
ans =

   12    3
    4    5
    6    7
```

* Matrix transpose

```
>> transpose(A)
ans =

   11    3    5
    2    4    6
```

* Create reange of values

```
>> v = 1:0.1:2
v =

    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000    1.6000    1.7000    1.8000    1.9000    2.0000
```

```
>> ones(2,3)
ans =

   1   1   1
   1   1   1

>> zeros(2,3)
ans =

   0   0   0
   0   0   0

```

* Random numbers with uniform distribution between 0 and 1

```
>> rand(2, 3)
ans =

   8.2018e-01   3.1833e-01   4.9587e-01
   4.4852e-03   4.3401e-01   8.8013e-01
```

* Gaussian random (normal distribution)

```
>> randn(2, 3)
ans =

   0.6886  -1.2203   1.0237
   0.8038  -2.0504   1.5572
```

* Historgram

```
>> w = -6 * sqrt(10) * randn(1, 10000);
>> hist(w)
```


```
>> eye(4)
ans =

Diagonal Matrix

   1   0   0   0
   0   1   0   0
   0   0   1   0
   0   0   0   1

```

```
>> A = [11 2; 3 4; 5 6]
A =

   11    2
    3    4
    5    6

>> sz = size(A)   % returns a 2 element vector
sz = 
   3  2
```

```
>> size(A, 1)
>> size(A, 2)

>> length(A)   % size of the longest dimension, usually applied only to vectors

>> pwd             % print working directory
>> cd /some/place  % change directory
>> ls              % list content of the directory

>> load flat_prices.dat        % space separated data file, creates a variable called flat_prices
>> A = csvread("flat_prices.csv")

>> who   % list existing variables
>> whos  % list variables with types as well
>> clear var  % will remove the variable var
>> clear    % removes all the variables
>> save hello.mat v;        % save the content of variable v to a Matlab file
>> load hello.mat           % loads the data back to the v variable
>> save hello.txt v -ascii  % save data in text (ASCII) format

>> A(3,2)       % access element of a matrix (row 3 column 2)
>> A(2,:)       % the second row
>> A(:,2)       % second column
>> A([1 3], :)  % rows 1 and 3

% one can also assign to such slices
>> A = [A, [100; 101; 102]];   % append another column to the right
>> C = [A, B]   % attach B to the right of A (side by side)
>> C = [A  B]   % the same
>> C = [A; B]   % attach B under A
>> A(:)   % flatten all the values of A into a vector
```


```
A * B   % matrix multiplcation
A .* B  % element-wise multiplication
A .^ 2  % element-wise squaring
1 ./ v  % create new matrix (or just vector?) with the 1/x for each element.
log(v)  % element-wise log
exp(v)  % element-wise exp
abs(v)  % element-wise abs
-v      % element-wise

A'      % transpose
val = max(v)         % returns the maximum value
[val, ind] = max(v)  % return the maximum value and its index
% for a matrix it will return column-wise max.

v < 3    % element-wise returns 1 or 0 for each element (true or false)
find(v < 3)  % return the indexes of the elements less than 3

A = magic(3)  % returns a magic square  (not used for ml, but nice to use for demos)
[rows, colums] = find(A >= 7)
sum(v)
prod(v)
floor(v)
ceil(v)
max(A, [], 1)  % column-wise max

sum(A, 1)   % sum each colum
sum(A, 2)   % sum each row
A . eye(9)  % element-wise product of the matrix with the identity matrix leaves only the values in the diagonal
sum(sum(A . eye(9)))  % sums all the columnt and all the lines to give the total of the values of the main diagonal
sum(sum(A . flipud(eye(9)))) % sum of elements in the other diagonal   (flip up down)
pinv(A)    % the invers of A
pinv(A) * A  % the identity matrix, up to a small rounding error

```



# Octave
{id: octave}


## Octave install
{id: octave-install}

```
apt-get install octave
```

## Octave interactive shell
{id: octave-interactive-shell}



## Math
{id: octave-math}

```
%  a comment

2 + 3    % 5
2 ^ 3    % 8
2 / 3    % 0.6667
```

## Logical operations
{id: octave-logical-operations}

```
0        % false
1        % true

==       % Is equal?
~=       % Is NOT equal?
3 == 3   % 1
3 == 4   % 0
3 ~= 3   % 0
3 ~= 4   % 1
1 && 0   % 0  (logical and)
1 && 2   % 1  (logical and)
1 || 0   % 1  (logical or)
~1       % 0  (logical not)
~2       % 0
~0       % 1
```

## Octave change interactive prompt
{id: octave-change-prompt}

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
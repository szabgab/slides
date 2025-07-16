# Your Salary is in Danger - Short-Circuit

* short circuit

```
If perl already knows the final value of a boolean expression after computing
only part of it, perl will NOT calculate the rest of the expression:
```

```
if ($my_money > 1_000_000 or $my_salary > 10_000) {
    # I can live well
}
```



```
if ($my_money > 1_000_000 or $my_salary++ > 10_000) {
    # I can live well
}
```





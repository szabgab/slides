# Arrays conclusion

```
x := [3]int{}               // 3-long arrays with default 0 values
x := [...]int{2, 7, 4}      // 3-long array with values
x := [3]int{2, 7, 4}        // same, but with unnecessary duplication of information
z := x[2]                    // access element 
x[2] = 42                   // assign to element
x[4]                        // out-of-range index: compile-time or run-time error
for i, v := range array {}  // iterator over index and value 
```



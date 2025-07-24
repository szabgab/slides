# Syntax of if statement

* else
* elsif
* indentation


{} are always required



```perl
if (COND) {
    STATEMENTs;
}


if (COND) {
    STATEMENTs;
} else {
    STATEMENTs;
}

if (COND_1) {
    A_STATEMENTs;
} else {
    if (COND_2) {
        B_STATEMENTs;
    } else {
        if (COND_3) {
            C_STATEMENTs;
        } else {
            D_STATEMENTs;
        }
    }
}


if (COND_1) {
    A_STATEMENTs;
} elsif (COND_2) {
    B_STATEMENTs;
} elsif (COND_3) {
    C_STATEMENTs;
} else {
    D_STATEMENTs;
}
```

[Comparing scalars in Perl](https://perlmaven.com/comparing-scalars-in-perl)



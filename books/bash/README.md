## bash length of string

```
expr length $var

length_of_var=$(expr length $var)
echo $length_of_var
```


## bash function

```
main () {
    echo "Hello World!"
}

main "$@"
```

## Loop over numbers

```
for i in {0..2..1}
    do
       echo "Welcome $i times"
done
```

```
    for i in $(seq 1 2 10)
    do
        echo "Welcome $i times"
    done
```



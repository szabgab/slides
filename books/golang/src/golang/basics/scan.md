# Scan input strings from STDIN

* STDIN
* Scan


We'll have a lot more to say about getting input from the user, but in order to be able to write some useful code, let's introduce a simple way to get input from the user. For this we need to declare a variable first to be a `string`. Then we call the `Scan` function and give the variable as a parameter. More precisely we pass a pointer to the variable to the function by prefixing it with `&`. Later we'll discuss pointers as well, for now all you need to know is that `Scan` will wait till the  user types in something and presses ENTER. Then all the content will be in the variable. 


* [fmt.Scan](https://golang.org/pkg/fmt/#Scan)

{% embed include file="src/examples/scan/scan.go" %}



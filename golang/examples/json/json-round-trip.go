package main

import (
    "fmt"
    "encoding/json"
)

func main() {
    var person = map[string]string{}
    person["name"] = "Foo Bar"
    person["email"] = "foo@bar.com"
    //fmt.Println(person)
    mystr, _ := json.Marshal(person)
    fmt.Printf("%T\n", mystr)
    //fmt.Printf("%s", json.Marshal(person))
}

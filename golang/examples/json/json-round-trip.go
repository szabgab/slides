package main

import (
    "fmt"
    "encoding/json"
)

func main() {
    var person = map[string]string{}
    person["name"] = "Foo Bar"
    person["email"] = "foo@bar.com"
    fmt.Println(person)
    fmt.Println(json.Marshal(person))
}


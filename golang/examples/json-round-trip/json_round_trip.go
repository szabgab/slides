package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var person = map[string]string{}
	person["name"] = "Foo Bar"
	person["email"] = "foo@bar.com"
	fmt.Println(person)
	myjson, err := json.Marshal(person)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("%T %s\n", myjson, myjson)
	reborn := make(map[string]string)
	err = json.Unmarshal(myjson, &reborn)
	fmt.Printf("%v", reborn)
}

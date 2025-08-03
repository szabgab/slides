package main

import "fmt"

type aPerson struct {
	name string
}

func (p *aPerson) changeName(newName string) {
	fmt.Printf("Old name: %v\n", p.name)
	p.name = newName
	fmt.Printf("New name: %v\n", p.name)
}

func main() {
	joe := aPerson{name: "Joe"}
	fmt.Println(joe)
	joe.changeName("Jane")
	fmt.Println(joe)
}

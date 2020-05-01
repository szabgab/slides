package main

import (
	"fmt"
	"os"
	"text/template"
)

func main() {
	tmpl, err := template.ParseFiles("if.txt")
	if err != nil {
		panic(err)
	}

	person := personType{
		Name:  "Jane",
		Email: "jena@code-maven.com",
	}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}
	fmt.Println("-----------------------------------------------------------")

	person = personType{
		Name: "Joe",
	}
	err = tmpl.Execute(os.Stdout, person)
	if err != nil {
		panic(err)
	}

}

type personType struct {
	Name  string
	Email string
}
